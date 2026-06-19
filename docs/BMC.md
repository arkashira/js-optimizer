# Business Model Canvas – **js‑optimizer**

| **Key Partners** | **Key Activities** | **Key Resources** |
|------------------|--------------------|-------------------|
| • **Rust community & contributors** – maintain the Rust toolchain and provide low‑level performance expertise. | • Develop and maintain the core optimizer (Rust + SWC). | • Source code repository (`arkashira/js-optimizer`). |
| • **SWC project** – upstream parser/transformer library. | • Integrate SWC updates and ensure compatibility. | • Build & CI pipelines (GitHub Actions, Docker images). |
| • **Node.js ecosystem** – npm registry, tooling authors. | • Publish and version npm packages. | • Documentation site (GitHub Pages). |
| • **Cloud CI/CD providers** (GitHub, GitLab, Azure Pipelines). | • Provide SDKs & CLI for CI integration. | • Test datasets (auto, messages, instr‑resp, query‑resp). |
| • **Enterprise tooling partners** (Webpack, Vite, Turborepo). | • Run performance benchmarks & regression testing. | • Community forum / Discord channel. |
| • **Axentx internal teams** – Sales/BD, QA, Validation. | • Gather market feedback & validate paying use‑cases. | • Funding & shared BRAIN (pgvector) for product knowledge. |

| **Value Proposition** | **Customer Segments** |
|-----------------------|-----------------------|
| • **Blazing‑fast compilation** – Rust‑based engine + SWC yields 2‑5× faster builds vs. pure JS tools. | • Front‑end engineering teams building large SPAs/MPAs. |
| • **Zero‑config optimization** – Automatic dead‑code elimination, minification, and tree‑shaking without extra plugins. | • Build‑tool vendors (Webpack, Vite, Rollup) seeking a high‑performance optimizer plugin. |
| • **Seamless integration** – Drop‑in npm package (`js-optimizer`) works with existing `npm`/`yarn`/`pnpm` workflows. | • CI/CD providers & DevOps teams that need faster pipelines. |
| • **Deterministic output** – Guarantees identical bundles across environments, aiding reproducible builds. | • Enterprises with strict performance SLAs for web delivery. |
| • **Open‑source core + commercial support** – Free community edition, paid support & enterprise features (e.g., custom rule sets, analytics). | • Open‑source contributors who want to extend the optimizer. |

| **Channels** | **Revenue Streams** |
|--------------|---------------------|
| • **npm registry** – primary distribution point. | • **Subscription SaaS** – hosted optimizer API (pay‑per‑build or tiered). |
| • **GitHub Releases & Docs** – self‑hosted binary & CLI. | • **Enterprise License** – on‑premise binary with SLA, priority patches. |
| • **Developer conferences & webinars** – demos & workshops. | • **Professional Services** – integration consulting, custom rule development. |
| • **Partner marketplaces** (Webpack plugin store, Vite plugins). | • **Support contracts** – 24/7 email/Slack support, SLAs. |
| • **Content marketing** – blog posts, case studies, benchmark reports. | • **Training & certification** – paid courses for teams. |

| **Cost Structure** |
|--------------------|
| • **Personnel** – Rust/TS engineers, QA, DevOps, product manager. |
| • **Infrastructure** – CI/CD runners, artifact storage, hosted optimizer API (compute & bandwidth). |
| • **Open‑source licensing compliance** – legal & audit. |
| • **Marketing & community** – events, sponsorships, content creation. |
| • **Partner program incentives** – revenue share with plugin marketplaces. |
| • **Support & SLA commitments** – on‑call staff, ticketing system. |

--- 

*Prepared by the Senior Product/Engineering Lead, Axentx – 2026‑06‑19*
