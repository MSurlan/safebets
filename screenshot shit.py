import pathlib

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import csv
import numpy as np
import os
import PIL
from selenium.webdriver.common.by import By
from PIL import Image
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import cv2
import matplotlib.pyplot as plt


##########################################################################################################################################################
# url = "https://sports.bwin.com/de-at/sports"
# driver.get(url)
# time.sleep(2)
# DOESNT WORK ASDKJADOIAJOIDLUHASLOIUDAJSLOUIDJHASULOIDHASLOIUDh #driver.execute_script('''return document.querySelector("#cdk-overlay-backdrop vn-backdrop cdk-overlay-backdrop-showing").querySelector("span[class='ui-icon theme-ex ng-star-inserted']")''').click() #admiral
#time.sleep(3)
##########################################################################################################################################################

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
        quoten = div.find_elements(By.CLASS_NAME, 'EventOddButton-styles-odd-button')

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
        for q in quoten:
            location = q.location
            size = q.size
            x = location['x']
            y = location['y']
            width = location['x'] + size['width']
            height = location['y'] + size['height']
            im = Image.open(imgpath)
            im = im.crop((int(x), int(y), int(width), int(height)))
            imgpath3 = f"images/traindata/image{counter3}.png"
            counter3 += 1
            im.save(imgpath3)
        for i in range(1,40):
            try:
                element = driver.find_element(By.XPATH,f"//*[@id='app']/main/main/section/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div/div/div[{i}]")  ## new div of all the div games i guess? EventRow-styles-event-row
                location = element.location
                size = element.size
                x = location['x']
                y = location['y']
                width = location['x'] + size['width']
                height = location['y'] + size['height']
                im = Image.open(imgpath)
                im = im.crop((int(x), int(y), int(width), int(height)))
                imgpath2 = f"images/tipico/image{counter2}.png"
                counter2 += 1
                im.save(imgpath2)
                # Do something with the element
            except NoSuchElementException:
                # Handle the case where the element is not found
                pass

        # Program-styles-program Program-styles-desktop

        # img2 = Image.open(imgpath)
        # width, height = img2.size
        # left = 300
        # top = height / 2
        # right = 2000
        # bottom = height
        # img2 = img2.crop((left, top, right, bottom))
        # img2.save("images/tipico/test2.png")

##########################################################################################################################################################
# data_dir = pathlib.Path(r"images/").with_suffix('')
# image_count = len(list(data_dir.glob('*/*.png')))
# print(image_count)
# tipico = list(data_dir.glob('tipico/*'))
# # img = PIL.Image.open(str(tipico[0]))
# # img.show()
# batch_size = 50
# img_height = 180
# img_width = 180
#
# train_ds = tf.keras.utils.image_dataset_from_directory(
#     data_dir,
#     validation_split=0.2,
#     subset="training",
#     seed=123,
#     image_size=(img_height, img_width),
#     batch_size=batch_size)
# val_ds = tf.keras.utils.image_dataset_from_directory(
#     data_dir,
#     validation_split=0.2,
#     subset="validation",
#     seed=123,
#     image_size=(img_height,img_width),
#     batch_size=batch_size)
#
# class_names = train_ds.class_names
# print(class_names)
#
# plt.figure(figsize=(10,10))
# for images, labels in train_ds.take(1):
#     for i in range(9):
#         ax = plt.subplot(3,3,i+1)
#         plt.imshow(images[1].numpy().astype("uint8"))
#         plt.title(class_names[labels[i]])
#         plt.axis("off")
# for image_batch, labels_batch in train_ds:
#   print(image_batch.shape)
#   print(labels_batch.shape)
#   break
#
# normalization_layer = tf.keras.layers.Rescaling(1./255)
#
# normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
# image_batch, labels_batch = next(iter(normalized_ds))
# first_image = image_batch[0]
# # Notice the pixel values are now in `[0,1]`.
# print(np.min(first_image), np.max(first_image))
# # print(tf.__version__)
#
# AUTOTUNE = tf.data.AUTOTUNE
#
# train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
# val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
# num_classes = 5
#
# model = tf.keras.Sequential([
#   tf.keras.layers.Rescaling(1./255),
#   tf.keras.layers.Conv2D(32, 3, activation='relu'),
#   tf.keras.layers.MaxPooling2D(),
#   tf.keras.layers.Conv2D(32, 3, activation='relu'),
#   tf.keras.layers.MaxPooling2D(),
#   tf.keras.layers.Conv2D(32, 3, activation='relu'),
#   tf.keras.layers.MaxPooling2D(),
#   tf.keras.layers.Flatten(),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(num_classes)
# ])
#
# model.compile(
#   optimizer='adam',
#   loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#   metrics=['accuracy'])
#
# model.fit(
#   train_ds,
#   validation_data=val_ds,
#   epochs=3
# )
# list_ds = tf.data.Dataset.list_files(str(data_dir/'*/*'), shuffle=False)
# list_ds = list_ds.shuffle(image_count, reshuffle_each_iteration=False)
# for f in list_ds.take(5):
#   print(f.numpy())
#
# class_names = np.array(sorted([item.name for item in data_dir.glob('*') if item.name != "LICENSE.txt"]))
# print(class_names)
# val_size = int(image_count * 0.2)
# train_ds = list_ds.skip(val_size)
# val_ds = list_ds.take(val_size)
# print(tf.data.experimental.cardinality(train_ds).numpy())
# print(tf.data.experimental.cardinality(val_ds).numpy())
