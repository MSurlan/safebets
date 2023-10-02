import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get('https://sports.admiral.at/de/sportwetten/fussball/champions-league?filter=betting')
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,"sc-dcJsrY gFLvup"))).click()

all_games = driver.find_elements(By.TAG_NAME, 'button')

for a in all_games:
    print(a.text)



#driver.quit()

