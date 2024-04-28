#!/bin/bash

# Run ruff check
echo "Running ruff check..."
ruff check

# Run ruff format
echo "Running ruff format..."
ruff format

# Run mypy
echo "Running mypy..."
mypy llm_core/

# Run pytest
echo "Running pytest..."
pytest test/