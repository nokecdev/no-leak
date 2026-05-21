# no-leaks (prototype)

⚠️ This project is currently in early development stage (prototype).
It is **not production-ready**, has not been tested in real-world environments, and should **not be used in production or security-critical workflows**.

Core validation logic is still incomplete and currently relies on hardcoded checks. Full regex-based scanning and rule system is under active development.

---

# What is no-leaks?

no-leaks is a lightweight developer tool designed to help prevent accidental exposure of secrets such as API keys, tokens, passwords, and other sensitive data before they are committed to a repository.

---

# Current status

- Basic hook integration works
- Simple hardcoded validation is implemented
- Core scanning engine is under development
- Regex + rule-based detection system is planned (JSON-based config)

---

# Planned features

- Regex-based secret detection
- JSON configuration for custom rules
- API key & token detection patterns
- Staged file scanning (git diff based)
- Ignore rules (.no_leaksignore)
- CLI usage independent from git hooks

---

# Installation (development version)

Run the install script:

```bash
sh install_hook.sh