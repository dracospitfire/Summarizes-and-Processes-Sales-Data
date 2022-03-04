#! /usr/bin/env python3

import os
import requests

url = 'http://localhost/fruits/'
path = "supplier-data/descriptions/"

for file in os.listdir(path):
    if file.endswith(".txt"):
        image_name = file.replace("txt", "jpeg")
        file = open(os.path.join(path, file))
        text = file.readlines()
        fruit_des = {}
        fruit_des.update({"name":text[0].strip("\n")})
        fruit_des.update({"weight":text[1].strip(" lbs\n")})
        fruit_des.update({"description":text[2].strip("\n")})
        fruit_des.update({"image_name":image_name})
        status = requests.post(url, data = fruit_des)
        print(status.status_code)

