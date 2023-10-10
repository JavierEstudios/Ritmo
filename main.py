import json

url = "https://github.com/JavierEstudios/ritmo/blob/3d78a3056ab875dbdb0d8d061cfad0bfe645c802/canciones.json"

file = open(url)

data = json.load(file)

for i in data["canciones"]:
    print (i)

file.close()
