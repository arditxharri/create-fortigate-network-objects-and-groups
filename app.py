from flask import Flask, render_template, request, redirect, url_for
import re
import pandas as pd

app = Flask(__name__)

def is_valid_ipv4(ip):
    """Check if a string is a valid IPv4 address."""
    pattern = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
    if pattern.match(ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False

def create_firewall_config(ip_list, object_list_name, group_name, add_to_existing_group):
    firewall_config = []
    for ip in ip_list:
        firewall_config.append(f'edit "{object_list_name}_{ip}"\n'
                               f'    set subnet {ip}/32\n'
                               f'next\n')
    
    addrgrp_config = f'config firewall addrgrp\n'
    if add_to_existing_group:
        group_choice = request.form.get('existing_group')
        if group_choice:
            addrgrp_config += f'    edit "{group_choice}"\n'
            for ip in ip_list:
                addrgrp_config += f'        append member "{object_list_name}_{ip}"\n'
            addrgrp_config += f'    next\n'
        else:
            addrgrp_config += f'    edit "{request.form.get("new_group_name")}"\n'
            for ip in ip_list:
                addrgrp_config += f'        append member "{object_list_name}_{ip}"\n'
            addrgrp_config += f'    next\n'
    else:
        addrgrp_config += f'    edit "{group_name}"\n'
        for ip in ip_list:
            addrgrp_config += f'        append member "{object_list_name}_{ip}"\n'
        addrgrp_config += f'    next\n'
    
    addrgrp_config += f'end'
    
    firewall_config.append(addrgrp_config)
    
    return firewall_config

def extract_ips_from_dataframe(df):
    ip_list = []
    for column in df.columns:
        for cell in df[column]:
            if isinstance(cell, str):
                ip_list.extend(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', cell))
    return ip_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        ip_input = request.form.get('ip_input')

        # Check if file is uploaded
        if uploaded_file:
            # Check if the file is a text file
            if uploaded_file.filename.endswith('.txt'):
                # Read IP addresses from the text file
                ip_list = re.findall(r'[0-9]+(?:\.[0-9]+){3}', uploaded_file.read().decode('utf-8'))
            elif uploaded_file.filename.endswith(('.xls', '.xlsx')):
                # Read IP addresses from Excel file using pandas
                df = pd.read_excel(uploaded_file)
                ip_list = extract_ips_from_dataframe(df)
        else:
            ip_list = []

        # Check IP addresses entered manually
        if ip_input:
            ip_list.extend(re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip_input))

        # Validate IPv4 addresses
        valid_ips = [ip for ip in ip_list if is_valid_ipv4(ip)]

        if not valid_ips:
            # No valid IP addresses found
            return redirect(url_for('invalid_ip_error'))

        object_list_name = request.form.get('object_list_name')
        group_name = request.form.get('group_name')
        add_to_existing_group = request.form.get('add_to_existing_group') == 'yes'

        firewall_config = create_firewall_config(valid_ips, object_list_name, group_name, add_to_existing_group)
        return render_template('result.html', config=firewall_config)
    return render_template('index.html')

@app.route('/invalid_ip_error')
def invalid_ip_error():
    return render_template('invalid_ip_error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
