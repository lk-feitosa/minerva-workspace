# Security Policy

## Supported Versions

Security fixes and updates are applied to the latest commit on the `main` branch.

| Version / Branch | Supported          |
| ---------------- | ------------------ |
| `main`           | :white_check_mark: |
| Older releases   | :x:                |

---

## Reporting a Vulnerability

**Please do not report security vulnerabilities or secret leaks in public issues or pull requests.**

If you discover a security vulnerability, credential exposure, or exploit in this repository or its associated agent skills:

1. **GitHub Security Advisory (Preferred):**  
   Use the **"Report a vulnerability"** button directly in the repository's **Security** tab to submit a private report.
2. **Direct Contact:**  
   If private reporting is unavailable, reach out directly to the maintainer via GitHub profile ([@lk-feitosa](https://github.com/lk-feitosa)).

### What to include in your report:
- Clear description of the vulnerability or security boundary bypass.
- Steps to reproduce or proof of concept.
- Affected skill, MCP server configuration, or script (`setup.bat`, `setup.ps1`, `setup.sh`).
- Suggested mitigations or patches (if available).

Please sanitize all sensitive data (such as API keys, personal access tokens, and private paths) from your logs before sending.

---

## Security Boundaries & Agent Safeguards

This repository configures autonomous and semi-autonomous AI coding agents (**Antigravity**, **Claude Code**, **Codex**, **Maestri**). To maintain operational safety, the following boundaries are enforced:

1. **Local Loopback Only:**  
   All MCP servers and telemetry tools (`ai-memory`, `painel-agents`, `rea`) bind strictly to `127.0.0.1` and communicate via `stdio` or authenticated local IPC. They are never exposed to public network interfaces.
2. **Credential Isolation:**  
   API keys, authentication headers, session states, and database locks (`.ai-memory/`, `.env*`, `*.session`, `*.lock`) are strictly git-ignored and must never be committed to source control.
3. **Execution Boundaries:**  
   Agents run with the permissions of the host user. Scripts provided in `skills/` and `toolkits/` should be reviewed before executing commands against untrusted codebases or external binaries.
