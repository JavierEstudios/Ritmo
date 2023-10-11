import json
import requests

headers = {'Accept': 'application/json'}

url = ("https://github.com/JavierEstudios/ritmo/blob/ee5e98cb912da4fa1b3738b87477ecb0486b7ba0/canciones.json")

file = requests.get(url, headers=headers)

#url = ("canciones.json")

#file = open(canciones.json)

data = file.json()

for i in data:
    print(i, ":", data[i])

file.close()
