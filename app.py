from flask import Flask, render_template, request
import re

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_input = request.form['ip_input']
        ip_list = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip_input)
        object_list_name = request.form['object_list_name']
        group_name = request.form['group_name']
        add_to_existing_group = request.form.get('add_to_existing_group') == 'yes'
        firewall_config = create_firewall_config(ip_list, object_list_name, group_name, add_to_existing_group)
        return render_template('result.html', config=firewall_config)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
