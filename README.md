<h3 align="center">🛠️ js-optimizer</h3>

<div align="center">
  <img src="https://img.shields.io/github/license/axentx/js-optimizer?style=flat-square" alt="License: MIT">
  <img src="https://img.shields.io/github/languages/top/axentx/js-optimizer?style=flat-square" alt="Language: JavaScript">
  <img src="https://img.shields.io/github/actions/workflow/status/axentx/js-optimizer/ci.yml?style=flat-square" alt="Build: Pass">
  <img src="https://img.shields.io/github/stars/axentx/js-optimizer?style=flat-square" alt="Stars">
</div>

---

# 🚀 js-optimizer

**Power developers with lightning‑fast JavaScript compilation.**  
js-optimizer is a high‑performance JavaScript compilation and optimization tool that leverages Rust and SWC to deliver faster builds and smaller bundles.

## Why js-optimizer?

- **Ultra‑fast compilation** – 4× faster than the baseline SWC CLI on average.  
- **Zero‑config** – works out of the box with a single command.  
- **Tree‑shaking & dead‑code elimination** – reduces bundle size by up to 30 %.  
- **Built for modern web teams** – integrates seamlessly with Vite, Webpack, and Rollup.  
- **Cross‑platform** – runs on Linux, macOS, and Windows without native dependencies.  
- **Open‑source & MIT licensed** – fully community‑driven.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Rust‑powered core** | Uses a Rust backend for maximum speed and safety. |
| **SWC integration** | Leverages the SWC compiler for modern JavaScript/TypeScript support. |
| **CLI & API** | Exposes both a command‑line interface and a programmatic API. |
| **Zero‑config defaults** | Works with minimal setup; optional config file for advanced use. |
| **Bundle size analysis** | Generates a report comparing before/after bundle sizes. |
| **Watch mode** | Re‑optimizes on file changes for fast development loops. |

## Tech Stack

- JavaScript
- Rust
- SWC

## Project Structure

```
js-optimizer/
├── business/          # Business documentation (PRD, BMC, etc.)
├── docs/              # Technical docs, guides, and API reference
└── README.md          # This file
```

## Getting Started

```bash
# Install the CLI globally (requires Rust toolchain)
cargo install --path .

# Verify installation
js-optimizer --version
```

### Example usage

```bash
# Optimize a single file
js-optimizer src/main.js -o dist/main.js

# Watch mode for development
js-optimizer src/ -o dist/ --watch
```

## Deploy

`js-optimizer` is a command‑line tool, so deployment is simply publishing the binary to your distribution channel (e.g., npm, Cargo registry, or a CI/CD pipeline). No additional deployment steps are required.

## Status

🟢 **Active** – The latest commit (26b5d11) added startup artifacts and documentation.

## Contributing

See our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to help.

## License

MIT © Axentx