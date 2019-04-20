from selenium import webdriver
from time import sleep

usr = #enter user name
pwd = #enter password

driver = webdriver.Chrome()
driver.get('https://erp.skit.ac.in/signin/')
username_box = driver.find_element_by_name("username")
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element_by_xpath("//*[@id='login-box']/form/div/input")
login_box.click()

menu = driver.find_element_by_xpath("/html/body/div[2]/aside[1]/section/ul/li[11]/a")
menu.click()
attendance = driver.find_element_by_xpath("/html/body/div[2]/aside[1]/section/ul/li[11]/ul/li/a")
attendance.click()


print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")

