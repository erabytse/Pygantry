# 🏗️ Pygantry
**The ultra-lightweight Python container engine.**

[![CI](https://github.com/erabytse/Pygantry/actions/workflows/ci.yml/badge.svg)](https://github.com/erabytse/Pygantry/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/pygantry.svg)](https://pypi.org/project/pygantry/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Docker-like simplicity for Python projects — without the overhead.**

Why ship a whole Linux OS with Docker when you only need a Python environment? 
**Pygantry** packages your app and its dependencies into a portable, relocatable "Gantry" that works anywhere.

## 🚀 Quick Start

```cmd
git clone https://github.com/erabytse/Pygantry.git
cd Pygantry

:: Windows (no installation needed)
1. **Init:** `pyg init --name my_app`
2. **Build:** `pyg build`
3. **Run:** `pyg run`
4. **Ship:** `pyg ship` -> Get a lightweight ZIP and send it!

```

## 🌟 Why Pygantry?
- **Small:** 15MB vs 500MB+ for Docker.
- **Simple:** No daemon, no sudo, just Python.
- **Portable:** Move your folder anywhere, it just works.


## ⚠️ Honest Limitations

Feature                            Status

✅ Works on same machine           Fully supported

⚠️ Relocation to another machine   Requires same Python version installed on target

❌ Full Docker replacement         Not a security sandbox — use for deployment simplicity only


💡 Philosophy: Pygantry solves deployment friction, not security isolation. Perfect for internal tools, prototypes, and edge devices where Docker is too heavy.


## 📦 Installation (optional)

```bash
pip install pygantry
pyg --help
```

## 🌍 Community

⭐ Star if you like lightweight Python tools!
🐞 Issues welcome — we respond within 24h
📜 MIT License — free for commercial use


Pygantry v1.2 — Simple by design
Part of **[erabytse](https://erabytse.github.io)** — a quiet rebellion against digital waste.

---

## 💙 Support 

If you use and value this tool, consider supporting its development:  
[![Sponsor](https://img.shields.io/badge/sponsor-erabytse-181717?logo=github)](https://github.com/sponsors/takouzlo)


[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-green)](https://flask.palletsprojects.com)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)](https://typescriptlang.org)
[![AI](https://img.shields.io/badge/AI-ML-orange)](https://pytorch.org)
[![Founder](https://img.shields.io/badge/Founder-erabytse-purple)](https://github.com/erabytse)
