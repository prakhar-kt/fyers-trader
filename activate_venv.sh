#!/bin/bash
# Deactivate any existing virtual environment
deactivate 2>/dev/null || true
conda deactivate 2>/dev/null || true

# Activate the fyers-trader pipenv virtual environment
source /Users/hobbes/.local/share/virtualenvs/fyers-trader-h2H7aZVq/bin/activate

echo "✓ Virtual environment activated!"
echo "Python: $(which python)"
echo "Python version: $(python --version)"
