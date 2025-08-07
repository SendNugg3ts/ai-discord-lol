.ONESHELL:
SHELL := /bin/bash
venv:
	uv venv .venv --python 3.12 && \
	source .venv/bin/activate && \
	uv sync --active --extra dev && \
	uv pip install --upgrade pip setuptools wheel toml && \
	uv pip install -e . --no-cache-dir && \
	uv lock

run:
	python src/main.py