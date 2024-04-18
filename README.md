This simple script is used to create network object and add them to a group in FortiGate cli. It generates the commands necessary for you. 
This is useful if u want to create multiple IP's and add them to the same object group (or network obejct group).
This app uses Python3 and Flask.


To use this app:
1.	Cd in the directory: `cd create-fortigate-network-objects-and-groups`
2.	`chmod +x flask_install_script.sh`
3.	Run the script: `/. flask_install_script.sh`
4.	After the script finishes run: `python3 app.py` *(note that you must be in the directory: **create-fortigate-network-objects-and-groups** to run it).*

# Create FortiGate Network Objects and Groups

This Python Flask application simplifies the creation of network objects and their inclusion in groups for FortiGate firewalls. Designed for ease of use, it provides a straightforward interface for generating the necessary commands to configure multiple IP addresses within a single object group or network object group.

## Features:

- **Upload Files:** Easily upload text files or Excel spreadsheets containing IP addresses for quick processing.
- **Manual Entry:** Enter IP addresses manually through a simple form interface.
- **Validation:** Automatically validates IPv4 addresses to ensure accurate configuration.
- **Customization:** Define object list names, group names, and choose whether to append to an existing group or create a new one.
- **Clear Feedback:** Receive clear feedback on invalid IP addresses to streamline the configuration process.
- **CLI Command Generation:** Generates FortiGate CLI commands for creating network objects and adding them to groups, ready for implementation.

## Usage:

1. Clone the repository.
2. Run the provided installation script to set up the Flask environment and install the required packages.
3. Launch the application with Python3.
4. Input IP addresses through file upload or manual entry, customize configuration options, and generate CLI commands.
5. Copy the generated commands and apply them to your FortiGate firewall for seamless network configuration.

## Requirements:

- Python 3
- Flask
- pandas
- Regular expressions (re)
- Openpyxl

## Get Started:

Clone the repository and streamline your FortiGate firewall configuration process today!

