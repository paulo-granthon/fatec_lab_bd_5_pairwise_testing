#!/bin/bash

# Check if the virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate the virtual environment
# shellcheck disable=SC1091
source venv/bin/activate

# Install the requirements
if [ ! -f "requirements.txt" ]; then
    echo "Creating requirements.txt with pytest..."
    echo "pytest" >requirements.txt
fi

pip install -r requirements.txt

# Run the tests
echo "Running tests..."
PYTHONPATH=$(pwd) pytest tests

# Deactivate the virtual environment
deactivate
