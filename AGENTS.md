# Repository Guidelines

## Project Structure & Module Organization
This repository is a compact tutorial workspace with two top-level files:
- `sqlite_basics.py`: runnable Python example showing SQLite setup, table creation, inserts, and queries.
- `Tutorial_3.pptx`: lecture/tutorial slides related to the script.

Keep new code examples in the repository root unless the project grows. If more scripts are added, group them under `examples/` and keep slide or document assets under `docs/`.

## Build, Test, and Development Commands
No build system is required. Use Python directly:
- `python3 sqlite_basics.py`: runs the SQLite demo end-to-end.
- `python3 -m py_compile sqlite_basics.py`: quick syntax validation.

If you add dependencies later, document setup in this file (for example with a `requirements.txt` and a virtual environment command).

## Coding Style & Naming Conventions
Follow standard Python conventions:
- 4-space indentation, no tabs.
- `snake_case` for functions/variables (`print_table`, `table_name`).
- `UPPER_SNAKE_CASE` for constants.
- Keep functions short and focused; prefer clear names over comments.

Recommended formatting/linting when available:
- `black .` for formatting.
- `ruff check .` for linting.

## Testing Guidelines
There is currently no formal test suite. For this tutorial repository:
- Validate by running `python3 sqlite_basics.py` and checking printed table/query output.
- When adding tests, use `pytest` with files named `test_*.py` (for example, `test_sqlite_basics.py`).
- Prefer small, deterministic tests (e.g., in-memory SQLite databases).

## Commit & Pull Request Guidelines
Git history is not available in this folder, so adopt this convention going forward:
- Commit format: `<type>: <short description>` (examples: `feat: add join query example`, `fix: enable foreign keys before inserts`).
- Keep commits focused on one logical change.

For pull requests, include:
- What changed and why.
- How to run/verify (`python3 sqlite_basics.py`).
- Sample output or screenshots when behavior/output changes.
