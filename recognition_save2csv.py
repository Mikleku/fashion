"""
скрипт предварительно загруженные на сервер изображения(коллекция указана в настройках) загоняет в модель распознования одежды
результаты записывает в папку data/название коллекции.csv
"""
import Algorithmia
import os
import csv
import settings

fashion_dir = settings.collection_name
data_set=[]
client = Algorithmia.client(settings.client_key)
dir = client.dir("data://.my/" + fashion_dir)


for file in dir.files():
    input = {
        "image": "data://" + file.path,
        "model": "small"
    }

    algo = client.algo('algorithmiahq/DeepFashion/1.2.2')
    data = algo.pipe(input)
    for a in data.result['articles']:
        el= dict(
            img_url = file.path,
            article_name = a["article_name"],
            confidence = a["confidence"],
            bounding_box = a["bounding_box"],
            output = data.result["output"]
        )
        data_set.append(el)


SAVEFILE = "data/" + fashion_dir + ".csv"

with open(SAVEFILE, "w", newline="") as file:
    columns = ["img_url","article_name", "confidence", "bounding_box",  "output" ]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    writer.writerows(data_set)

