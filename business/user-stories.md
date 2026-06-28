## 📄 `user-stories.md`

### Epic 1 – **Fast & Reliable Build Pipeline**
| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|----------------------|------------|
| 1 | **As a front‑end developer, I want the optimizer to compile my ES2023 code to ES5 in under 200 ms for a 500 KB bundle, so that I can iterate faster during development.** | - Input: a 500 KB bundle containing modern syntax.<br>- Output: ES5 bundle ≤ 200 ms on a typical CI runner (2 vCPU, 4 GB RAM).<br>- Source‑maps are generated and line numbers match original files.<br>- No runtime errors when the output is executed in Chrome 80+. | S |
| 2 | **As a CI/CD engineer, I want the tool to run as a single binary with zero‑install steps, so that I can add it to any pipeline without extra dependencies.** | - Distribution includes pre‑built binaries for Linux, macOS, Windows (x86_64 & arm64).<br>- `js-optimizer --help` works immediately after download.<br>- No external Node, Java, or Python runtime required.<br>- Binary size ≤ 15 MB. | S |
| 3 | **As a build manager, I want deterministic output (same hash for same input) across machines, so that caching works reliably.** | - Given identical input files and flags, the SHA‑256 hash of the output bundle is identical on macOS, Linux, and Windows.<br>- Cache‑key can be generated from the hash alone.<br>- Documented “deterministic mode” flag. | M |
| 4 | **As a QA lead, I want the optimizer to fail fast with clear error messages when it encounters unsupported syntax, so that developers can fix issues quickly.** | - Errors include file name, line/column, and a short description.<br>- Exit code != 0 on any compilation error.<br>- Errors are emitted in JSON (`--output-format=json`) for CI parsing.<br>- No silent drops of code. | M |

### Epic 2 – **Advanced Optimizations & Tree‑Shaking**
| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|----------------------|------------|
| 5 | **As a performance engineer, I want dead‑code elimination (tree‑shaking) to remove unused exports, so that bundle size shrinks.** | - When an exported function is never imported, it is omitted from the final bundle.<br>- Size reduction ≥ 15 % on a typical React app (≈ 200 KB before).<br>- No functional regression (unit tests pass).<br>- Option to disable via `--no‑tree‑shake`. | M |
| 6 | **As a front‑end architect, I want automatic inlining of small constants and functions, so that runtime overhead is minimized.** | - Constants ≤ 8 bytes are inlined at call sites.<br>- Functions marked `/* @inline */` are inlined when size ≤ 32 bytes.<br>- Generated source‑map reflects inlined code.<br>- Benchmarks show ≤ 5 % speed‑up on micro‑benchmarks. | L |
| 7 | **As a security reviewer, I want the optimizer to perform safe minification (no mangling of public API names unless opted‑in), so that downstream consumers are not broken.** | - By default, only local identifiers are mangled.<br>- Public exports retain original names unless `--mangle‑exports` is set.<br>- A “dry‑run” mode lists renamed symbols without writing output.<br>- No change in behavior of exported functions. | M |

### Epic 3 – **Developer Experience & Extensibility**
| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|----------------------|------------|
| 8 | **As a VS Code user, I want an editor plugin that runs the optimizer on‑save, so that I see the optimized bundle instantly.** | - Plugin installs via VS Code Marketplace.<br>- On file save, runs `js-optimizer` with project config.<br>- Shows a notification with size delta and time taken.<br>- Allows disabling per‑workspace. | M |
| 9 | **As a library author, I want a configuration file (`js-optimizer.config.json`) to fine‑tune passes, so that I can enable/disable specific optimizations per project.** | - Config supports `treeShake`, `inline`, `minify`, `target`, `sourceMap` fields.<br>- CLI automatically discovers the file at project root.<br>- Validation errors are reported with line numbers.<br>- Example config shipped with repo. | S |
| 10 | **As a DevOps engineer, I want the optimizer to expose a JSON‑API (`--json-report`) summarizing applied transforms, so that I can feed metrics into our monitoring dashboards.** | - Report includes input size, output size, time per pass, and list of removed symbols.<br>- Schema is versioned (`v1`).<br>- Can be piped to `jq` or sent to a HTTP endpoint via `--post-report`. | M |
| 11 | **As a contributor, I want the codebase to be written in idiomatic Rust with comprehensive tests, so that I can safely extend it.** | - 80 %+ code coverage (unit + integration).<br>- CI runs `cargo clippy`, `cargo fmt`, and `cargo test` on all platforms.<br>- CONTRIBUTING.md outlines how to add a new optimization pass.<br>- Linting fails the PR if coverage drops. | L |
| 12 | **As a product manager, I want a “preview mode” that outputs both the original and optimized bundles side‑by‑side, so that stakeholders can visually compare size and performance impact.** | - `--preview` writes `original.js` and `optimized.js` to a `preview/` folder.<br>- Generates an HTML diff report with size bars and gzip stats.<br>- No changes to the original build output path. | S |

---  

*All stories are scoped for a **MVP** release of **js‑optimizer**. Complexity estimates follow the internal sizing rubric (S = ≤ 2 person‑days, M = ≈ 5 person‑days, L = ≈ 10 person‑days).*