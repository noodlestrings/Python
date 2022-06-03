from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # select browser

driver.maximize_window()

driver.get("https://www.freecodecamp.org/learn")
# driver.close() #closes tab; .quit() exits
print(driver.title)

search = driver.find_element(By.CLASS_NAME, value="ais-SearchBox-input")
search.send_keys("python")
search.send_keys(Keys.RETURN)

time.sleep(2)
postFeed = driver.find_elements(By.CLASS_NAME, value="post-card-title")
for post in postFeed:
    print(post.text)

time.sleep(5)
driver.quit()
