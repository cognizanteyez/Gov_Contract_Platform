# Security Policy

## Supported Scope

This repository is a public prototype and learning artifact. It is not a production service and should not be used to store real customer, government, account, or procurement data.

## Reporting a Vulnerability

Please do not post suspected credentials, personal data, or exploit details in a public issue. Contact the maintainer through [PatternBridge Systems](https://patternbridgesystems.vip) with a concise description of the concern and the affected file or component.

## Credential and Data Rules

- Use environment variables for API keys, session secrets, and connection strings.
- Do not commit `.env` files, local databases, cached records, or customer information.
- Rotate a credential immediately if it may have been exposed.
- Treat prior Git history as potentially discoverable after a secret is removed from the current files.
