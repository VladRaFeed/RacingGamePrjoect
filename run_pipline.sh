#!/bin/bash

# Встановлення кольорів для виводу
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # Без кольору

echo "Starting local CI/CD pipeline..."

# Перевірка наявності віртуального оточення
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Creating and activating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
fi

# Встановлення залежностей
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Встановлення pre-commit
echo "Installing pre-commit hook..."
pre-commit install

# Запуск усіх перевірок через pre-commit
echo "Running pre-commit checks..."
pre-commit run --all-files
if [ $? -eq 0 ]; then
    echo -e "${GREEN}All checks passed successfully!${NC}"
else
    echo -e "${RED}Checks failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Pipeline completed successfully!${NC}"