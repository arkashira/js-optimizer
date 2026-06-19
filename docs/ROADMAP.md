# ROADMAP.md – **js‑optimizer**

---

## Vision
Deliver a **high‑performance JavaScript compilation and optimization tool** built on **Rust + SWC** that dramatically reduces bundle size and improves runtime speed for modern web applications, while integrating seamlessly into existing developer toolchains.

---

## Milestones Overview

| Milestone | Target Release | Core Theme | MVP‑Critical Items* |
|-----------|----------------|------------|----------------------|
| **MVP** | **2026‑09‑30** | Foundations & Core Optimizations | ✅ |
| **v1.0** | 2026‑12‑15 | Ecosystem Integration & Advanced Optimizations | — |
| **v2.0** | 2027‑04‑30 | Enterprise‑grade Features & Observability | — |

\*Items marked **✅** are required for the MVP launch; without them the product cannot be released.

---

## 1️⃣ MVP – Foundations & Core Optimizations (Due 2026‑09‑30)

| Category | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **Compilation Engine** | Rust‑based SWC wrapper | Expose SWC parser/transformer via a safe Rust API. | Unit tests cover parsing of ES2022 syntax, no panics. |
| **CLI** | `js-opt` command | Simple CLI that accepts input file(s) and outputs optimized code. | `js-opt src/index.js -o dist/index.js` runs in < 200 ms for a 200 KB file. |
| **Optimization Passes** | *Dead‑code elimination* | Remove unreachable code branches. | Bundle size reduction ≥ 10 % on benchmark suite. |
| | *Constant folding* | Pre‑compute constant expressions. | Same as above, verified on numeric heavy modules. |
| | *Minify (identifiers & whitespace)* | Produce production‑ready minified output. | Output passes `uglify‑js` baseline size test. |
| **Configuration** | `js-opt.config.json` | Declarative config for enabling/disabling passes. | CLI respects config; defaults enable all MVP passes. |
| **Testing & Quality** | Test harness | End‑to‑end tests on a curated set of real‑world packages (React, Vue, Node libs). | ≥ 90 % pass rate, CI green on every push. |
| **Documentation** | Quick‑Start Guide | README section with install, usage, config examples. | New user can run `npm i -g js-optimizer && js-opt -h` successfully. |
| **Packaging** | NPM distribution (binary + JS wrapper) | Publish `js-optimizer` package with pre‑built binaries for Linux/macOS/Windows (x86_64, aarch64). | `npm publish` succeeds; `npm install` works without native‑build tools. |

### MVP Success Metrics
- **Performance:** ≥ 2× faster than `swc-cli` on the same input (measured on CI hardware).  
- **Size Reduction:** ≥ 15 % average bundle size reduction vs. baseline (no‑opt).  
- **Stability:** < 0.5 % crash rate across 10 k CI runs.  

---

## 2️⃣ v1.0 – Ecosystem Integration & Advanced Optimizations (Due 2026‑12‑15)

| Theme | Feature | Description | Deliverable |
|-------|---------|-------------|-------------|
| **Toolchain Plugins** | Webpack loader | `js-opt-loader` for seamless integration. | Works with Webpack 5, passes tests in a sample React app. |
| | Vite plugin | `vite-plugin-js-opt`. | Zero‑config usage in Vite projects. |
| **Advanced Passes** | Tree‑shaking (ESM) | Remove unused exports across module boundaries. | Bundle size reduction ≥ 20 % on large monorepos. |
| | Inline caching & hoisting | Optimize repeated helper functions. | Runtime speedup ≥ 10 % in benchmark loops. |
| **Source Maps** | Preserve accurate source maps through all passes. | Developers can debug optimized code. | Source maps map back to original lines with < 5 ms overhead. |
| **Incremental Compilation** | Cache ASTs & transformed modules. | Faster rebuilds in watch mode. | Re‑compile time ≤ 50 ms for unchanged files. |
| **CI/CD Integration** | GitHub Action | Auto‑run optimizer on PRs, enforce size budget. | Action passes on Axentx internal repos. |
| **Telemetry (opt‑in)** | Usage stats (opt‑in) | Collect pass usage & performance data for continuous improvement. | Dashboard shows aggregated metrics. |
| **Documentation Expansion** | API reference, plugin guides, migration docs. | Comprehensive docs site (Docusaurus). | Docs build passes CI. |

---

## 3️⃣ v2.0 – Enterprise‑grade Features & Observability (Due 2027‑04‑30)

| Theme | Feature | Description | Success Criteria |
|-------|---------|-------------|-------------------|
| **Enterprise Security** | Signed binaries & SBOM | Provide reproducible builds, SPDX SBOM. | Passes Axentx security audit. |
| **Policy Engine** | Configurable rule sets (e.g., forbid certain globals). | Enables compliance enforcement. | Policy violations block CI builds. |
| **Distributed Build Service** | Remote compilation daemon (gRPC). | Offload heavy optimization to a cluster. | 5× speedup for > 5 MB bundles. |
| **Observability** | Real‑time dashboard (bundle size, compile time, pass effectiveness). | Ops can monitor usage across orgs. | Dashboard updates within 30 s of a run. |
| **Language Extensions** | Support for TypeScript, JSX, and newer TC39 proposals. | Broader market coverage. | Correctly compiles TS 4.9+ projects. |
| **Custom Pass SDK** | Public API for users to write their own optimization passes in Rust or JS. | Extensibility for niche use‑cases. | Sample custom pass passes CI. |
| **Enterprise Support** | SLA‑backed support portal, priority issue triage. | Monetization enablement. | Support tickets resolved < 24 h. |

---

## Release Process (All Milestones)

1. **Feature Freeze** – 2 weeks before target date.  
2. **Beta Program** – Invite internal Axentx teams & 3 external partners.  
3. **Performance Gate** – Must meet the quantitative metrics listed per milestone.  
4. **Security Review** – Automated static analysis + manual audit.  
5. **Final QA** – End‑to‑end regression suite across OS/arch matrix.  
6. **Tag & Publish** – Semantic versioning (`v0.x.0` for MVP, `v1.0.0`, `v2.0.0`).  

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Rust‑SWC API breaking changes | Delays MVP | Pin SWC version, maintain a thin compatibility layer. |
| Binary distribution size | Adoption friction | Use `musl` static builds, provide `npm`‑only JS fallback. |
| Performance regressions on large codebases | Customer churn | Continuous benchmark suite, automated alerts. |
| Insufficient ecosystem adoption | Revenue impact | Early partner program, co‑marketing with Webpack/Vite maintainers. |

---

## Success Metrics (Post‑Launch)

| Metric | Target (12 mo) |
|--------|----------------|
| **Monthly Active Users** | 5,000 |
| **Average Bundle Size Reduction** | 18 % |
| **Average Compile Time Reduction** | 2.5× vs. baseline |
| **Retention Rate** | 85 % |
| **Revenue (subscription)** | $250k ARR |

--- 

*Prepared by the Senior Product/Engineering Lead, Axentx – js‑optimizer team*
