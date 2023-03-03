from selenium import webdriver
from time import sleep

tab1= webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")#In executable path give the path of chromedriver that you have downloaded. In my case it is in downloads.
tab2= webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")
tab3= webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")
tab4= webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")#In executable path give the path of chromedriver that you have downloaded. In my case it is in downloads.
tab5= webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")
tab6= webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe")

link = input("Enter Youtube Shorts URL: ")
lenght = input("Enter time length of short: ")

tab1.get(link)
tab2.get(link)
tab3.get(link)
tab4.get(link)
tab5.get(link)
tab6.get(link)
while True:
    sleep(eval(lenght))
    tab1.refresh()
    tab2.refresh()
    tab3.refresh()
    tab4.refresh()
    tab5.refresh()
    tab6.refresh()