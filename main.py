import json
import requests

#headers = {'Accept': 'application/json'}
#url = ('https://github.com/JavierEstudios/ritmo/blob/ee5e98cb912da4fa1b3738b87477ecb0486b7ba0/canciones.json')
#file = requests.get(url)
#data = file.json()

#print(data)

file = open("canciones.json")
data = json.load(file)

cc = 1
while cc < 7.5:
    i = 0
    for canciones in data['canciones']:
        if data['canciones'][i]['pst_cc'] == cc:
            print ("Nombre: ",data['canciones'][i]['nombre'],", pack: ",data['canciones'][i]['pack'],", dificultad: ",data['canciones'][i]['pst'],", lado: ",data['canciones'][i]['lado'],", duración: ",data['canciones'][i]['length'])
        i = i+1
    cc = cc+0.5

#for canciones in data:
#    print(data['canciones'])

##file.close()
