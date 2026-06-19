# STORIES.md – js‑optimizer  

**Product:** js‑optimizer – A high‑performance JavaScript compilation and optimization tool built with Rust and SWC, aimed at accelerating development workflows and reducing bundle size for modern web applications.  

---  

## Epic 1 – Core Compilation Engine  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1.1 | **As a front‑end developer, I want to compile my ES2023 source files to ES5, so that my code runs on legacy browsers.** | - CLI flag `--target es5` produces syntactically correct ES5 output.<br>- Source maps are generated and correctly map to original files.<br>- Compilation time for a 500 KB bundle ≤ 150 ms on a typical CI runner (2 vCPU, 8 GB RAM). |
| 1.2 | **As a build engineer, I want the optimizer to accept a directory of entry points, so that I can batch‑process an entire project.** | - CLI accepts `--input <dir>` and recursively discovers `.js`/`.mjs` files.<br>- Output directory mirrors input structure preserving relative paths.<br>- Logs a summary: files processed, total time, average size reduction. |
| 1.3 | **As a performance‑focused developer, I want the tool to run in parallel across CPU cores, so that large codebases compile faster.** | - Utilises Rust’s Rayon thread pool.<br>- `--jobs <n>` caps parallelism; default = number of logical CPUs.<br>- No race conditions; output files are deterministic across runs. |
| 1.4 | **As a CI/CD pipeline owner, I want the compiler to exit with a non‑zero status on syntax errors, so that builds fail fast.** | - Invalid JavaScript triggers an error message with file, line, column.<br>- Process exits with status > 0.<br>- No partial output files are written on failure. |

## Epic 2 – Advanced Optimizations  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 2.1 | **As a front‑end engineer, I want dead‑code elimination, so that unused modules are removed from the bundle.** | - `--optimize dead-code` removes functions/variables never referenced.<br>- Tree‑shaking respects `export`/`import` semantics and side‑effect annotations (`/* @__PURE__ */`). |
| 2.2 | **As a performance engineer, I want minification of identifiers and literals, so that bundle size is minimized.** | - `--minify` shortens local variable names, removes whitespace/comments, and folds constant expressions.<br>- Output size reduction ≥ 30 % on a typical React app benchmark. |
| 2.3 | **As a developer, I want optional JSX/TSX transformation, so that I can compile React components without a separate Babel step.** | - `--jsx` flag converts JSX to `React.createElement` (or `h` for preact) using SWC’s JSX parser.<br>- TypeScript syntax is preserved when `--ts` is also supplied. |
| 2.4 | **As a security‑concerned engineer, I want source‑code obfuscation as an opt‑in feature, so that intellectual property is harder to reverse‑engineer.** | - `--obfuscate` applies identifier renaming and string literal encoding.<br>- Obfuscation is deterministic given a seed (`--seed <value>`). |
| 2.5 | **As a build optimizer, I want bundle‑splitting based on dynamic imports, so that only needed code is loaded at runtime.** | - `--code-split` generates separate output files for each dynamic `import()` boundary.<br>- Generates a manifest JSON mapping chunks to entry points. |

## Epic 3 – Integration & Developer Experience  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 3.1 | **As a VS Code user, I want a language‑server protocol (LSP) plugin, so that I can get on‑the‑fly diagnostics from js‑optimizer.** | - LSP server starts with `js-optimizer --lsp`.<br>- Provides syntax errors, unused variable warnings, and quick‑fix suggestions.<br>- Works with the official VS Code extension scaffold. |
| 3.2 | **As a package maintainer, I want the tool to be publishable as an npm package with a binary for major platforms, so that users can install it easily.** | - `npm publish` produces a package with pre‑built binaries for Linux, macOS, Windows (x86_64).<br>- Post‑install script verifies binary integrity (SHA‑256). |
| 3.3 | **As a CI pipeline author, I want a Docker image that contains the optimizer, so that I can run it in isolated environments.** | - Dockerfile builds a minimal `scratch`‑based image with the compiled binary.<br>- Image size ≤ 30 MB.<br>- `docker run --rm -v $(pwd):/src js-optimizer --input /src --output /out` works as documented. |
| 3.4 | **As a developer, I want a JSON‑based configuration file (`js-optimizer.config.json`), so that I can version‑control my build settings.** | - CLI automatically loads `js-optimizer.config.json` from the working directory.<br>- CLI flags override config values.<br>- Validation errors are reported with line/column numbers. |
| 3.5 | **As a product manager, I want usage telemetry (opt‑in) to be sent to our internal endpoint, so that we can measure adoption and performance.** | - `--telemetry` flag enables POST of anonymized metrics (runtime, input size, options used).<br>- Users can disable via `JS_OPTIMIZER_TELEMETRY=0` env var.<br>- No source code or personal data is transmitted. |

## Epic 4 – Quality Assurance & Release  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 4.1 | **As a QA engineer, I want a comprehensive test suite with unit, integration, and snapshot tests, so that regressions are caught early.** | - `cargo test` runs ≥ 200 unit tests covering each CLI flag.<br>- Integration tests compile a sample project and compare output against stored snapshots.<br>- CI pipeline fails on any test regression. |
| 4.2 | **As a release manager, I want automated semantic versioning based on commit messages, so that releases follow a predictable scheme.** | - `semantic-release` runs on merge to `main` and publishes a new npm version (major/minor/patch).<br>- Changelog is generated from conventional commits. |
| 4.3 | **As a security auditor, I want the binary to be reproducible builds, so that we can verify integrity.** | - Build process records `Cargo.lock` and source hash.<br>- `cargo build --release` produces identical binaries given the same environment (verified via SHA‑256). |

---  

### MVP Scope (first release)

1. **Epic 1 – Core Compilation Engine** (Stories 1.1‑1.4)  
2. **Epic 2 – Advanced Optimizations** (Stories 2.1‑2.3) – basic dead‑code elimination, minification, JSX/TSX support.  
3. **Epic 3 – Integration** (Stories 3.2‑3.4) – npm package, Docker image, config file.  

*Stories 2.4‑2.5, 3.1, 3.5, and all Epic 4 items are slated for post‑MVP iterations.*  

---  

*All stories are written to be independently testable, shippable, and traceable to the product backlog.*
