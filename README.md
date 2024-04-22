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

1. Clone this repo: `git clone https://github.com/arditxharri/create-fortigate-network-objects-and-groups.git`
2.	Cd in the directory: `cd create-fortigate-network-objects-and-groups`
3.	`chmod +x flask_install_script.sh`
4.	`python3 -m venv myenv`
5.	`source myenv/bin/activate`
6.	Run the script: `./flask_install_script.sh`
7.	`sudo firewall-cmd --zone=public --add-port=5000/tcp --permanent`
8.	`sudo firewall-cmd --reload`
9.	After the script finishes run: `python3 app.py` *(note that you must be in the directory: **create-fortigate-network-objects-and-groups** to run it).*
10.	Access you web app your computer IP on port 5000( Ex: if you pc'c IP is **192.168.1.10** you can access it at **http://192.168.1.10:5000**)

## Requirements:

- Python 3
- Flask
- pandas
- Regular expressions (re)
- Openpyxl

## Get Started:

Clone the repository and streamline your FortiGate firewall configuration process today!

