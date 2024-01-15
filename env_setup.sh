#!/bin/sh

# Check for Python installation
if [[ -x "$(command -v python3)" ]]; then
  echo "Python is installed."
else
  echo "Python is not installed."
  echo "Please visit https://www.python.org/downloads/ to install it."
  exit 1
fi

# Install dependencies
pip install python-dotenv
pip install requests
pip install pandas
