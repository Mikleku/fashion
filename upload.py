"""
скрипт загружает файлы на сервер для коллекции указанной в settings - collection name
"""
import Algorithmia
import os
import settings

dir = settings.collection_name
client = Algorithmia.client(settings.client_key)
cloud_dir = client.dir("data://.my/"+dir)
cloud_dir.create()

list = os.listdir(path="./pics/" + dir)
for l in list:
    client.file("data://.my/" + dir + "/" + l).putFile("pics/" + dir + "/" + l)
