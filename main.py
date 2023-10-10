import json
import requests

url = ("https://github.com/JavierEstudios/ritmo/blob/ee5e98cb912da4fa1b3738b87477ecb0486b7ba0/canciones.json")

file = requests.get(url)

data = file.json()

for i in data['canciones']:
    print (i)

file.close()
