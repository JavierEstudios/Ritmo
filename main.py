import json
import requests

headers = {'Accept': 'application/json'}
url = ('https://github.com/JavierEstudios/ritmo/blob/5cd4087de1440f4b9208647a2eda4980c7a715a3/canciones.json')
file = requests.get(url, headers)
data = file.json()

print(data)

""" file = open("canciones.json")
data = json.load(file)

## Valores predeterminados
cc = 'prs_cc'
mincc = 1
maxcc = 12
level = 'prs'

selectDone = False
dificultad = input("Introduzca la dificultad en la que quiere ordenar las canciones (pasado, presente, futuro o beyond): ")
while selectDone == False:
    selectDone = True
    if dificultad == 'pasado':
        cc = 'pst_cc'
        maxcc = 7
        level = 'pst'
    elif dificultad == 'presente':
        mincc = 3.5
        maxcc = 9.5
    elif dificultad == 'futuro':
        cc = 'ftr_cc'
        mincc = 7
        maxcc = 11.3
        level = 'ftr'
    elif dificultad == 'beyond':
        cc = 'byd_cc'
        mincc = 9.5
        level = 'byd'
    else:
        dificultad = input("Input no reconocido, vuelva a introducurlo: ")
        selectDone = False


while mincc <= maxcc:
    i = 0
    for canciones in data['canciones']:
        if data['canciones'][i][cc] == mincc:
            print ("Nombre: ",data['canciones'][i]['nombre'],", pack: ",data['canciones'][i]['pack'],", dificultad: ",data['canciones'][i][level],", bando: ",data['canciones'][i]['lado'],", duración: ",data['canciones'][i]['length'])
        i = i+1
    if mincc < 8:
        mincc = mincc+0.5
    else: mincc = round(mincc+0.1, 1) """

file.close()
