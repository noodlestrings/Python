from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get("https://www.apple.com/uk/macbook-air/")


time.sleep(5)
driver.quit()
