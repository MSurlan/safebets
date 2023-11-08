import pathlib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import numpy as np
import os
import PIL
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
    tipico_cookie_clicked = False
    betahome_cookie_clicked = False
    for row in reader:
        url = str(row[0])
        print(url)
        driver.get(url)
        time.sleep(2)
        if "tipico" in url and tipico_cookie_clicked == False :
            driver.execute_script('''return document.querySelector("#_evidon_banner").querySelector("button[id='_evidon-accept-button']")''').click()  # tipico
            tipico_cookie_clicked = True
        if "bet-at-home" in url and betahome_cookie_clicked == False:
            driver.execute_script('''return document.querySelector("#AppContainer").querySelector("button[class='CloseFirstAccessButton']")''').click()  # betathome
            betahome_cookie_clicked = True
        counter+=1
        imgpath = "images/image{}.png".format(counter)
        driver.save_screenshot(imgpath)
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
