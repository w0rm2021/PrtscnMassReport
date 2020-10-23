import os
import requests
from time import sleep
from random import seed, random

var_report = 0
id = input("[+] ID DO PRTSCN: ")

while 1:
    emailgerado = str(f"a{random()}") # EMAIL RANDOMICO
    r = requests.post(f"https://prnt.sc/reportabuse.php?id={id}&reason=1&email={emailgerado}@gmail.com")
    var_report += 1
    print(f"[+] {var_report} abusos reportados -> E-mail: {emailgerado}@gmail.com")