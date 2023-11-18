import pathlib

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import csv
import numpy as np
import pytesseract
import os
import PIL
from selenium.webdriver.common.by import By
from PIL import Image
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import cv2
import matplotlib.pyplot as plt



### take whole game div names and quotes and run through each div and save that in specific game folder! to differentiate the different games

##########################################################################################################################################################
options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)
with open('druglinks2.csv', newline="") as csvfiles:
    reader = csv.reader(csvfiles, delimiter=' ', quotechar='|')
    counter = 0
    counter2 = 0
    counter3 = 0
    tipico_cookie_clicked = False
    betathome_cookie_clicked = False
    for row in reader:
        url = str(row[0])
        print(url)
        driver.get(url)
        time.sleep(2)
        # div = driver.find_element(By.TAG_NAME, 'div') #EventOddButton-styles-odd-button //*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[4]
        #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[5]
        div = driver.find_element(By.TAG_NAME, 'div')
        #quoten = div.find_elements(By.CLASS_NAME, 'EventOddButton-styles-odd-button')
        games = div.find_elements(By.CLASS_NAME, 'SportsCompetitionsEvents-styles-competitions-events-block')
        if "tipico" in url and tipico_cookie_clicked == False :
            driver.execute_script('''return document.querySelector("#_evidon_banner").querySelector("button[id='_evidon-accept-button']")''').click()  # tipico
            tipico_cookie_clicked = True
        if "bet-at-home" in url and betathome_cookie_clicked == False:
            driver.execute_script('''return document.querySelector("#AppContainer").querySelector("button[class='CloseFirstAccessButton']")''').click()  # betathome
            betathome_cookie_clicked = True
        counter+=1
        counter2+=1
        counter3+=1

        imgpath = f"images/image{counter}.png"
        driver.save_screenshot(imgpath)
        # gamecounter = 1
        # for q in games:
        #     a = div.find_element(By.TAG_NAME,'a')
        #     quoten2 = a.find_elements(By.CLASS_NAME,'EventRow-styles-event-row')
        #     gamecounter += 1
        #     for q2 in quoten2:
        #         location = q2.location
        #         size = q2.size
        #         x = location['x']
        #         y = location['y']
        #         width = location['x'] + size['width']
        #         height = location['y'] + size['height']
        #         im = Image.open(imgpath)
        #         im = im.crop((int(x), int(y), int(width), int(height)))
        #         imgpath3 = f"images/traindata/{gamecounter}game{counter3}.png"
        #         counter3 += 1
        #         if np.std(im) > 1:
        #             im.save(imgpath3)


        for i in range(1,40):
            try:
                for k in range(2,10):
                    #element = driver.find_element(By.XPATH,f"//*[@id='app']/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[{i}]")  ## new div of all the div games i guess? EventRow-styles-event-row
                    element = driver.find_element(By.XPATH,f"//*[@id='app']/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[{i}]/a/div[{k}]")  ## new div of all the div games i guess? EventRow-styles-event-row
                    location = element.location
                    size = element.size
                    x = location['x']
                    y = location['y']
                    width = location['x'] + size['width']
                    height = location['y'] + size['height']
                    im = Image.open(imgpath)
                    im = im.crop((int(x), int(y), int(width), int(height)))
                    imgpath2 = f"images/tipico/GAME{i}image{counter2}.png"
                    counter2 += 1
                    if np.std(im) > 1:
                        im.save(imgpath2)
            except NoSuchElementException:
                pass


 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[1]/a/div[2]
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[1]/a/div[3]
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[1]/a/div[4]
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[1]/a/div[5]
 #-
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/a/div[2]
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/a/div[3]
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/a/div[4]
 #//*[@id="app"]/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/a/div[5]