# TECH_SPEC.md  

**Project:** `js-optimizer`  
**Owner:** Axentx – High‑Performance JavaScript Compilation & Optimization  
**Status:** Prototype → MVP → Production (target release v1.0)  
**Last Updated:** 2026‑06‑19  

---  

## 1. Overview  

`js-optimizer` is a command‑line and library tool that compiles, minifies, and performs advanced static optimizations on modern JavaScript/TypeScript codebases. It is built in **Rust** and leverages the **SWC** (Speedy Web Compiler) ecosystem for parsing, transformation, and code generation, providing:

* **Sub‑millisecond compilation** for large codebases (≥ 1 M LOC).  
* **Tree‑shaking**, dead‑code elimination, and constant folding across ES2024+ syntax.  
* **Source‑map preservation** for seamless debugging.  
* **Pluggable optimization passes** (e.g., React JSX, WebAssembly interop).  
* **CLI** for CI/CD pipelines and a **Rust crate** for embedding in other tools (e.g., bundlers, IDE extensions).  

The tool targets developers who need faster build times than Babel/TS‑c and tighter integration with Rust‑based back‑ends (e.g., `vLLM`, `SGLang`).  

---  

## 2. Architecture  

```
+-------------------+        +-------------------+        +-------------------+
|   CLI / Library   | <----> |   Core Engine     | <----> |   SWC Pipeline    |
| (bin/js-opt)      |        | (rust crate)      |        | (swc_ecma_parser)|
+-------------------+        +-------------------+        +-------------------+
        ^                           ^                           ^
        |                           |                           |
        |   Rust FFI (cbindgen)    |   Plugin Interface        |   SWC Passes
        |                           |   (dyn Trait objects)     |
        |                           |                           |
+-------------------+        +-------------------+        +-------------------+
|   Config Loader   | <----> |   Pass Manager    | <----> |   Optimizer Passes|
| (toml/json)       |        | (ordered exec)    |        | (tree‑shake, etc)|
+-------------------+        +-------------------+        +-------------------+
```

* **CLI / Library Layer** – Exposes `js-opt` binary and `js_optimizer` crate API. Handles argument parsing, config loading, and I/O (file, stdin/stdout, streams).  
* **Core Engine** – Coordinates the compilation pipeline, manages the pass manager, and interacts with SWC. Implemented in safe Rust with minimal `unsafe`.  
* **SWC Pipeline** – Re‑uses SWC’s parser, lexer, and code‑gen modules. All transformations are expressed as SWC `Fold`/`Visit` passes.  
* **Pass Manager** – Dynamically loads built‑in and third‑party optimizer passes via a trait object registry (`OptimizerPass`). Execution order is deterministic based on config priority.  
* **Config Loader** – Reads a TOML/JSON configuration file (`js-opt.toml`) that defines enabled passes, target environments (e.g., `es2022`, `node14`), source‑map options, and plugin paths.  

---  

## 3. Components  

| Component | Responsibility | Public API | Key Types |
|-----------|----------------|------------|-----------|
| **CLI (`src/bin/main.rs`)** | Argument parsing (`clap`), file I/O, logging (`tracing`) | `run(args: Args) -> Result<()>` | `Args`, `OutputMode` |
| **Library (`src/lib.rs`)** | Core entry point for embedding | `optimize(input: &str, cfg: &Config) -> Result<Output>` | `Config`, `Output` |
| **Config Loader (`src/config.rs`)** | Deserialize TOML/JSON into `Config` | `load(path: &Path) -> Result<Config>` | `Config`, `PassSpec` |
| **Pass Manager (`src/pass_manager.rs`)** | Register, order, and execute optimizer passes | `execute(ast: Module) -> Result<Module>` | `OptimizerPass` trait |
| **Built‑in Passes (`src/passes/*`)** | Tree‑shake, dead‑code elim, const‑fold, JSX transform, etc. | Implement `OptimizerPass` | `TreeShakePass`, `DeadCodePass`, … |
| **Plugin Loader (`src/plugin.rs`)** | Load external `.so`/`.dll` plugins at runtime | `load_plugin(path) -> Result<Box<dyn OptimizerPass>>` | `PluginMetadata` |
| **SWC Wrapper (`src/swc.rs`)** | Bridge to SWC parser & codegen | `parse(src) -> Result<Module>`; `print(ast) -> Result<String>` | `Module`, `SourceMap` |
| **Telemetry (`src/telemetry.rs`)** | Emit build metrics (time, size reduction) | `record(event: Event)` | `Metrics` |

---  

## 4. Data Model  

### 4.1 Core Types  

```rust
/// Full configuration for a run.
pub struct Config {
    pub target: TargetEnv,               // e.g., Es2024, Node14
    pub source_map: SourceMapConfig,     // Inline, External, None
    pub passes: Vec<PassSpec>,           // Ordered list of passes
    pub plugins: Vec<PathBuf>,           // Paths to dynamic plugins
    pub emit_metrics: bool,              // Enable telemetry
}

/// Specification of a single optimizer pass.
pub struct PassSpec {
    pub name: String,                    // Identifier, matches built‑in or plugin
    pub enabled: bool,
    pub options: toml::Value,            // Pass‑specific options
    pub priority: u32,                   // Lower runs earlier
}
```

### 4.2 Pass Interface  

```rust
/// Trait implemented by every optimizer pass.
pub trait OptimizerPass {
    /// Human readable name.
    fn name(&self) -> &str;

    /// Execute the pass on the AST.
    fn run(&self, ast: swc_ecma_ast::Module, ctx: &PassContext) -> Result<swc_ecma_ast::Module>;

    /// Optional hook for post‑run telemetry.
    fn after_run(&self, metrics: &mut PassMetrics) {}
}
```

### 4.3 Output  

```rust
pub struct Output {
    pub code: String,                    // Optimized JavaScript
    pub source_map: Option<String>,      // If generated
    pub metrics: Option<Metrics>,        // Size/time reductions
}
```

---  

## 5. Key APIs / Interfaces  

### 5.1 Library API (Rust Crate)

```rust
/// Optimize a JavaScript/TypeScript source string.
pub fn optimize(src: &str, cfg: &Config) -> Result<Output>;

/// Convenience: read from file, write to file.
pub fn optimize_file(input: &Path, output: &Path, cfg: &Config) -> Result<()>;
```

### 5.2 CLI Usage  

```bash
# Basic compilation
js-opt -i src/**/*.js -o dist/ --target es2024

# With custom config
js-opt --config js-opt.toml src/main.ts

# Enable plugins
js-opt --plugin ./plugins/custom_pass.so src/app.js
```

### 5.3 Plugin API (Dynamic Library)

A plugin must expose a C‑compatible symbol `create_pass` returning a boxed `OptimizerPass`:

```c
#[no_mangle]
pub extern "C" fn create_pass() -> *mut dyn OptimizerPass;
```

The plugin is compiled with `cbindgen` to generate the header for non‑Rust consumers.

---  

## 6. Technology Stack  

| Layer | Technology | Reason |
|-------|------------|--------|
| **Language** | Rust (edition 2021) | Zero‑cost abstractions, safety, native performance |
| **Parsing/Codegen** | SWC (`swc_ecma_parser`, `swc_ecma_codegen`) | Industry‑grade JS/TS parser, supports latest syntax |
| **CLI** | `clap` (v4), `tracing` (v0.2) | Declarative arg parsing, structured logging |
| **Config** | `serde` + `toml`/`serde_json` | Flexible, human‑readable configuration |
| **Dynamic Plugins** | `libloading` + `cbindgen` | Runtime extensibility without recompiling core |
| **Metrics** | `prometheus-client` (optional) | Export build metrics for CI dashboards |
| **Testing** | `cargo test`, `insta` snapshot testing | Guarantees deterministic transformations |
| **CI/CD** | GitHub Actions, Docker (multi‑stage) | Reproducible builds, cross‑platform binaries |
| **Packaging** | `cargo` crates.io, `npm` (via `wasm-pack` optional) | Rust crate for back‑ends, optional JS wrapper for npm |

---  

## 7. Dependencies  

| Crate | Version | License |
|-------|---------|---------|
| `swc_ecma_parser` | 0.150 | Apache‑2.0 |
| `swc_ecma_codegen` | 0.150 | Apache‑2.0 |
| `clap` | 4.4 | MIT |
| `serde` / `serde_derive` | 1.0 | MIT/Apache‑2.0 |
| `toml` | 0.8 | MIT |
| `tracing` | 0.2 | Apache‑2.0 |
| `libloading` | 0.8 | MIT |
| `cbindgen` | 0.26 | MIT |
| `prometheus-client` | 0.13 | Apache‑2.0 |
| `insta` | 1.34 | MIT |

All dependencies are compatible with the **MIT/Apache‑2.0** policy of Axentx.

---  

## 8. Deployment & Distribution  

| Artifact | Format | Distribution Channel |
|----------|--------|----------------------|
| **CLI Binary** | `js-opt` (Linux x86_64, macOS, Windows) | GitHub Releases, Docker (`ghcr.io/arkashira/js-optimizer:latest`) |
| **Rust Crate** | `js_optimizer` | crates.io (`js_optimizer = "0.1.0"`) |
| **NPM Wrapper (optional)** | `js-optimizer` (via `wasm-pack` producing a WASM binary) | npm registry (future expansion) |
| **Plugins** | Shared library (`.so`, `.dll`, `.dylib`) | Published under `arkashira/js-optimizer-plugins` repo |

### Docker Image (multi‑stage)

```Dockerfile
# Builder
FROM rust:1.78 as builder
WORKDIR /app
COPY . .
RUN cargo build --release

# Runtime
FROM debian:stable-slim
COPY --from=builder /app/target/release/js-opt /usr/local/bin/js-opt
ENTRYPOINT ["js-opt"]
```

The image size is ~45 MB (static linking stripped).  

---  

## 9. Security & Compliance  

* **Memory safety** – Rust guarantees no buffer over‑reads. All `unsafe` blocks are audited and limited to FFI with SWC.  
* **Sandboxing** – The optimizer never executes user code; it only parses and transforms ASTs.  
* **License compliance** – All third‑party crates are Apache‑2.0 or MIT; a `LICENSES.txt` is generated at build time via `cargo-about`.  
* **Supply‑chain** – Binaries are signed with GPG; CI publishes SBOM (CycloneDX) alongside each release.  

---  

## 10. Milestones  

| Milestone | Scope | Target |
|-----------|-------|--------|
| **MVP (v0.1)** | Core CLI, built‑in passes (tree‑shake, dead‑code, const‑fold), source‑map support | 2026‑07‑15 |
| **v0.5** | Plugin system, telemetry, Docker image, CI metrics | 2026‑08‑30 |
| **v1.0** | Full pass catalog, stable API, npm WASM wrapper, production‑grade docs | 2026‑10‑15 |
| **Post‑v1** | Community plugin marketplace, incremental compilation cache, integration with Axentx products (`vLLM`, `SGLang`) | Q4 2026 |

---  

## 11. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| **SWC breaking changes** | Compilation failures | Pin SWC to `0.150.x`; run nightly compatibility tests |
| **Plugin ABI drift** | Crashes at runtime | Use versioned C ABI (`create_pass_v1`); enforce semver on plugin interface |
| **Large codebase memory usage** | OOM on CI agents | Stream parsing mode (`swc_common::SourceMap::new` with `Arc`), optional `--max-memory` flag |
| **Incorrect source‑map offsets** | Debugging pain | Include exhaustive source‑map round‑trip tests in CI |

---  

## 12. Documentation  

* **User Guide** – `docs/USER_GUIDE.md` (installation, CLI flags, config examples).  
* **Developer Guide** – `docs/DEVELOPER.md` (adding passes, plugin development).  
* **API Reference** – generated via `cargo doc --no-deps`.  
* **Changelog** – `CHANGELOG.md` follows Keep a Changelog format.  

---  

## 13. Contact  

- **Product Owner:** `alice.smith@axentx.com`  
- **Lead Engineer:** `bob.lee@axentx.com`  
- **Slack:** `#js-optimizer` (Axentx workspace)  

---  

*Prepared by the Senior Product/Engineering Lead, Axentx – 2026‑06‑19*
