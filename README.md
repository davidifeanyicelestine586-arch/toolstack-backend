# ToolStack Backend

A small Python/FastAPI backend supporting the ToolStack technology-recommendation work.

## Overview

The current implementation exposes a simple API backed by a JSON tool catalog. It can return matching tools from a text query based on the tags defined in the catalog.

## Status

**Status:** Supporting / experimental backend project

The README describes the implementation currently present in the repository. Planned capabilities are not presented as completed functionality.

## Requirements

- Python 3
- pip

## Installation

Clone the repository and install the declared dependencies:

```bash
git clone https://github.com/davidifeanyicelestine586-arch/toolstack-backend.git
cd toolstack-backend
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Usage

Start the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload
```

The local API is available at `http://127.0.0.1:8000`.

Example endpoints:

- `GET /` — basic health response
- `GET /recommend?query=python` — returns catalog entries whose tags match the query

FastAPI also provides interactive API documentation at `/docs` while the development server is running.

## Configuration

The current implementation reads its tool catalog from `tools.json` and does not document a required secret or environment-variable contract.

Keep credentials, tokens, and local environment files outside version control.

## Testing

No automated test suite is currently documented. For basic verification, start the API and check the root and recommendation endpoints.

## Documentation

- [README](README.md) — project overview and setup
- [CONTRIBUTING](CONTRIBUTING.md) — contribution guidance
- [LICENSE](LICENSE) — MIT license

## Demo and downloads

- **Repository / download:** https://github.com/davidifeanyicelestine586-arch/toolstack-backend
- **Live demo:** Not currently available
- **Documentation:** https://github.com/davidifeanyicelestine586-arch/toolstack-backend/blob/main/README.md

## Support

Use the repository [issue tracker](https://github.com/davidifeanyicelestine586-arch/toolstack-backend/issues) for questions, bugs, and project discussion.

## License

MIT License. See [LICENSE](LICENSE).
