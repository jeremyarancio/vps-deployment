
default:
  @just --choose

format:
  uvx ruff check --fix
  uvx ruff format

type-check:
  uvx ty check

dev :
  uv run fastapi dev src/app/interface/api/main.py
