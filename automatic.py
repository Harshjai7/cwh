from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = " " #Give the url of the webpage you want to login 
username = " "
password = " "
driver = webdriver.chrome("")#Give the path of your chromedriver file
driver.get(url)
driver.maximize_window() #It will make the page to maximize screen
time.sleep(1) # This is for waiting for load . If your pc is slow give some more time in sleep 
driver.find_element(By.XPATH ,'#give the xpath by inspect the variable and right click and capy the xpath this is for username ').send_keys(username)
time.sleep(1) # This is for waiting for load . If your pc is slow give some more time in sleep 
driver.find_element(By.XPATH ,'#give the xpath by inspect the variable and right click and capy the xpath this is for password ').send_keys(password)
time.sleep(1) # This is for waiting for load . If your pc is slow give some more time in sleep
driver.find_element(By.XPATH ,'#give the xpath by inspect the variable and right click and capy the xpath this is for submit button ').click()
time.sleep(100)#give more seconds there so it wouldn't close soon 
# You can add more option there
driver.quit()# for closing the webpage
