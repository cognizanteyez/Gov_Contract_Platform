# Government Contract Opportunity Platform

> **Project status:** Prototype / learning project. This repository is a technical artifact, not a production-ready procurement, contracting, security, or decision-making system.

## Overview

This Flask-based prototype explores an authenticated workflow for discovering public government-contract opportunities. It combines a basic account flow, protected dashboard and contracts views, and a server-side search endpoint intended to query public opportunity data from SAM.gov.

The project demonstrates early work in business systems, user workflows, API-backed opportunity discovery, and government-procurement concepts.

## Current Capabilities

| Area | Current implementation |
|---|---|
| User access | Registration, login, logout, and session handling through Flask-Login. |
| Protected pages | Authenticated dashboard and contracts routes. |
| Opportunity search | A server-side endpoint intended to query public opportunity data using date, state, and ZIP-code inputs. |
| Data persistence | Flask-SQLAlchemy and migration scaffolding for local development. |

## Local Setup

This project is an early prototype and may require additional refinement before it runs in a modern production environment.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Set the following environment variables in your shell before running the application:

```bash
export SECRET_KEY="replace-with-a-long-random-value"
export DATABASE_URL="sqlite:///app.db"
export SAM_API_KEY="your-sam-gov-api-key"
python run.py
```

See [`.env.example`](.env.example) for variable names. Do not commit real credentials, database files, or environment files.

## Security and Data Handling

This repository is being maintained as a public technical portfolio artifact. It does not include production secrets or customer data. Local databases, cached data, and environment files are intentionally ignored.

If you identify a security concern, please review [`SECURITY.md`](SECURITY.md) before reporting it.

## Scope and Limitations

This prototype is not a substitute for official procurement sources, legal counsel, contracting guidance, security review, or production application hardening. Opportunity data, eligibility, deadlines, and compliance requirements should always be verified through official sources.

## Future Improvements

Potential next steps include dependency modernization, automated tests, secure deployment configuration, better API error handling, user-experience refinement, and documented data-retention practices.
