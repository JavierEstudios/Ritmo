import requests

url = ('https://raw.githubusercontent.com/JavierEstudios/ritmo/main/canciones.json')
file = requests.get(url)
data = file.json()

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
            cancion = data['canciones'][i]['nombre']
            pack = data['canciones'][i]['pack']
            coleccion = data['canciones'][i]['col']
            if coleccion == None: coleccion = 'Ninguna'
            nivel = data['canciones'][i][level]
            bando = data['canciones'][i]['lado']
            duracion = data['canciones'][i]['length']
            print ("Nombre: {0:43s} Pack: {1:22s} Colección: {2:20s} Dificultad: {3:3s} Bando: {4:9s} Duración: {5:7s}"
                   .format(cancion, pack, coleccion, nivel, bando, duracion))
        i = i+1
    if mincc < 8:
        mincc = mincc+0.5
    else: mincc = round(mincc+0.1, 1)

file.close()
