from selenium import webdriver
from time import sleep
from random import seed, random

var_report = 0

while 1:
    emailgerado = str(f"a{random()}") # EMAIL RANDOMICO
    browser = webdriver.Firefox() 
    link = input("[+] LINK DO PRTSCN: ")
    browser.get(link)
    browser.find_element_by_xpath('//*[@id="report-abuse"]/strong').click()
    browser.find_element_by_xpath('//*[@id="report-abuse-email"]').send_keys(f"{emailgerado}@gmail.com")
    browser.find_element_by_xpath('//*[@id="report-abuse-report"]').click()
    sleep(0.50)
    var_report += 1
    print(f"[+] {var_report} abusos reportados -> E-mail: {emailgerado}@gmail.com")
    browser.quit()