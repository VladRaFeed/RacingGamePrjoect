#!/bin/bash

echo "Starting local CI/CD pipeline..."

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create reports directory
echo "Creating reports directory..."
mkdir -p reports/pytest
mkdir -p reports/flake

# Run autopep8
echo "Running autopep8..."
autopep8 --in-place --aggressive --max-line-length=88 --ignore=E203 src/**/*.py

# Run flake8 and generate HTML report
echo "Running flake8..."
flake8 src/ --max-line-length=88 --extend-ignore=E203 --format=html --htmldir=reports/flake || { echo "Flake8 checks failed!"; exit 1; }

# Run pytest and generate HTML report
echo "Running pytest..."
pytest src/ --verbose --html=reports/pytest/report.html --self-contained-html || { echo "Pytest checks failed!"; exit 1; }

# Install pre-commit hook
echo "Installing pre-commit hook..."
pre-commit install

# Run pre-commit checks
echo "Running pre-commit checks..."
pre-commit run --all-files || { echo "Pre-commit checks failed!"; exit 1; }