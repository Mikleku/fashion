"""
данный скрипт берет изображения из collection_name
1)рисует на них боксы с одеждой и подписью, затем складывает в папку used
2)с каждого элемента одежды создает новое изображение в папке elements и шлепает туда основные цвета
"""
import settings
import csv
import ast
from scripts import boxplacer,colorsgetter

import cv2
import numpy as np
import scipy.misc




FILENAME = "./data/" + settings.collection_name + ".csv"
with open(FILENAME, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cords = ast.literal_eval(row['bounding_box'])
        artical_name = row['article_name']
        img_name = row["img_url"].split("/")[-1]
        img_path = "./pics/" + settings.collection_name + '/' + img_name
        new_img_path_name = "./pics/" + settings.collection_name + "_used/" + img_name
        new_img_path_color = "./pics/" + settings.collection_name + "_used/elements/"+artical_name + "_"+ img_name
        new_img_path_laplac = "./pics/" + settings.collection_name + "_used/elements/laplac/" + artical_name + "_" + img_name

        #Laplacian
        img0 = cv2.imread(new_img_path_color)
        gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(gray, (3, 3), 0)
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        scipy.misc.imsave(new_img_path_laplac, laplacian)


        #main data placers
        boxplacer.place_box(img_path, new_img_path_name, cords, artical_name)
        colorsgetter.put_colors(img_path,new_img_path_color,cords)





print("ok")


