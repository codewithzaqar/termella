# Contributing to Termella

First off, thank you for taking the time to contribute to **Termella** ❤️

Termella is a Python library focused on building elegant, expressive, and interactive terminal experiences. Every contribution—whether code, documentation, ideas, or bug reports—helps make the project better.

---

## 🚀 Ways to Contribute

You can contribute in many ways:

* Reporting bugs
* Suggesting new features or improvements
* Improving documentation
* Writing or improving code
* Reviewing pull requests
* Sharing Termella with others

---

## 🐛 Reporting Bugs

If you find a bug, please open an issue and include:

* A clear and descriptive title
* Steps to reproduce the issue
* Expected vs actual behavior
* Python version and operating system
* Any relevant error messages or screenshots

Before opening a new issue, please check if it has already been reported.

---

## 💡 Feature Requests

Feature ideas are welcome! When submitting a feature request:

* Describe the problem the feature solves
* Explain your proposed solution
* Include examples or mock usage if possible

Well-thought-out proposals are more likely to be accepted.

---

## 🧑‍💻 Development Setup

1. **Fork** the repository
2. **Clone** your fork locally:

   ```bash
   git clone https://github.com/your-username/termella.git
   cd termella
   ```
3. Create a **virtual environment** and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Install the project in editable mode (if applicable):

   ```bash
   pip install -e .
   ```

---

## 🌱 Branching Strategy

* `main` — stable, production-ready code
* Create a new branch for your work:

  ```bash
  git checkout -b feature/my-feature
  ```

Use descriptive branch names such as:

* `feature/select-menu`
* `fix/windows-input-bug`
* `docs/api-examples`

---

## ✅ Coding Guidelines

* Follow **PEP 8** style guidelines
* Write clear, readable, and well-documented code
* Prefer small, focused commits
* Avoid unnecessary abstractions
* Keep the API simple and expressive

If you add new functionality, please include:

* Docstrings
* Examples where appropriate
* Tests (if the project uses them)

---

## 🧪 Testing

Before submitting a pull request:

* Ensure existing tests pass
* Add tests for new functionality if applicable
* Manually test interactive terminal behavior when relevant

---

## 📦 Commit Messages

Use clear and consistent commit messages:

* `feat: add multi-select checkbox component`
* `fix: handle arrow keys on Windows`
* `docs: improve README examples`
* `refactor: simplify input handling`

---

## 🔁 Pull Requests

When opening a pull request:

* Describe **what** you changed and **why**
* Reference related issues (e.g. `Closes #12`)
* Keep PRs focused and reasonably sized
* Be open to feedback and requested changes

All pull requests are reviewed before merging.

---

## 🤝 Code of Conduct

By participating in this project, you agree to uphold a respectful and welcoming environment.

Be kind, constructive, and professional.

---

## ❤️ Thank You

Your time and effort are deeply appreciated.

Happy hacking, and enjoy building beautiful terminal experiences with **Termella** ✨
