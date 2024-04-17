#!/bin/bash

# Function to check if a package is installed
package_installed() {
    if [ "$(command -v "$1")" ]; then
        return 0
    else
        return 1
    fi
}

# Install or upgrade Python
if ! package_installed python3; then
    echo "Python not found. Installing..."
    if [ "$(command -v apt-get)" ]; then
        sudo apt-get update
        sudo apt-get install -y python3
    elif [ "$(command -v yum)" ]; then
        sudo yum install -y python3
    elif [ "$(command -v dnf)" ]; then
        sudo dnf install -y python3
    else
        echo "Unsupported package manager. Please install Python manually."
        exit 1
    fi
else
    echo "Python already installed. Checking for upgrades..."
    if [ "$(command -v apt-get)" ]; then
        sudo apt-get update
        sudo apt-get upgrade -y python3
    elif [ "$(command -v yum)" ]; then
        sudo yum upgrade -y python3
    elif [ "$(command -v dnf)" ]; then
        sudo dnf upgrade -y python3
    else
        echo "Unsupported package manager. Skipping Python upgrade."
    fi
fi

# Install or upgrade pip
echo "Installing or upgrading pip..."
sudo $(command -v python3) -m ensurepip --upgrade

# Check if virtual environment exists
if [ ! -d "myenv" ]; then
    # Create virtual environment
    echo "Creating virtual environment..."
    $(command -v python3) -m venv myenv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate

# Install or upgrade Flask
if ! $(command -v pip) show flask &> /dev/null; then
    echo "Flask not found. Installing..."
    pip install Flask
else
    echo "Flask already installed. Checking for upgrades..."
    pip install --upgrade Flask
fi

# Install or upgrade pandas
if ! $(command -v pip) show pandas &> /dev/null; then
    echo "pandas not found. Installing..."
    pip install pandas
else
    echo "pandas already installed. Checking for upgrades..."
    pip install --upgrade pandas
fi

# Create directory structure
echo "Creating directory structure..."
mkdir -p myflaskapp/static myflaskapp/templates

# Create a basic Flask app file if it doesn't exist
if [ ! -f "myflaskapp/app.py" ]; then
    echo "Creating basic Flask app file..."
    cat <<EOF > myflaskapp/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
EOF
fi

echo "Setup complete. You can now run your Flask app by executing 'python myflaskapp/app.py'."
