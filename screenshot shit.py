from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)
urls = []
url = "https://sports.bwin.com/de-at/sports"
driver.get(url)
#driver.execute_script('''return document.querySelector("#_evidon_banner").querySelector("button[id='_evidon-accept-button']")''').click() #tipico
#driver.execute_script('''return document.querySelector("#AppContainer").querySelector("button[class='CloseFirstAccessButton']")''').click() #betathome
time.sleep(3)
# DOESNT WORK ASDKJADOIAJOIDLUHASLOIUDAJSLOUIDJHASULOIDHASLOIUDh #driver.execute_script('''return document.querySelector("#cdk-overlay-backdrop vn-backdrop cdk-overlay-backdrop-showing").querySelector("span[class='ui-icon theme-ex ng-star-inserted']")''').click() #admiral
#time.sleep(3)

driver.save_screenshot("test12.png")