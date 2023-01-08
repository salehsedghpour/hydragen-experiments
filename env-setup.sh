#!/bin/bash
# This script prepare the virtual environment for the experiments.


# Check Python version
PYTHON_VERSION=$(python3.8 --version)
if [ "$PYTHON_VERSION" != "Python 3.8.10" ]
then
    echo "To be able to run the python scripts here, there should be Python 3.8.10 installed on your machine. Currently, $PYTHON_VERSION is installed on your machine."
    echo "If the current version is 3.8.x, you can continute running the script by simply changing this script, but it is not guranteed if it will work."
    echo "To install the right version (Python 3.8.10), visit (https://python.org)."
    exit
fi

python3 -m venv ./.venv

source ./.venv/bin/activate

pip3 install -r ./requirements.txt > /dev/null 2>&1

echo "The virtual environment is ready!"
