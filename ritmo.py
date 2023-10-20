import requests

def funcionPrincipal():
    ## Valores predeterminados para que python no se queje
    cc = 'prs_cc'
    mincc = 1
    maxcc = 12
    level = 'prs'
    ## Packs en el juego
    listaPacks = ["Eternal Core","Crimson Solace","Arcaea","Memory Archive","Ambivalent Vision","Vicious Labyrinth","Binary Enfold","Luminous Sky","Absolute Reason","Adverse Prelude","Sunset Radiance","Extend Archive","Black Fate","Ephemeral Page","Esoteric Order","Divided Heart","Final Verdict","Silent Answer","World Extend","Lasting Eden"]

    ## Preguntar si mostrar los packs del juego
    print("El Programa muestra el listado de canciones de un pack del juego, ordenadas por dificultad.")
    mostrarPacks = input("¿Quiere ver la lista de packs? (si o no): ")
    if mostrarPacks == 'si':
        for i in listaPacks:
            print(i)

    ## Seleccionar el pack del que se muestran las canciones
    pack = input("Introduzca de que pack quiere que sean las canciones. Puede dejar el campo vacio para mostrar todas las canciones: ")
    selectPack = False
    packCorrecto = False
    if pack == '':
        print("Mostrando todas las canciones")
        packCorrecto = True
    while packCorrecto == False:
        for i in listaPacks:
            if i == pack: 
                selectPack = True
                packCorrecto = True
                print("Mostrando las canciones de " + pack)
        if packCorrecto == False:
            print(pack + " no es un input valido")
            pack = input("Introduzca de que pack quiere que sean las canciones: ")

    ## Seleccionar la dificultad en la que se recorren las canciones
    selectDiff = False
    dificultad = input("Introduzca la dificultad en la que quiere ordenar las canciones (pasado, presente, futuro o beyond): ")
    while selectDiff == False:
        selectDiff = True
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
            selectDiff = False
    if selectPack: cancionesPorPack(cc, mincc, maxcc, level, pack)
    else: todasLasCanciones(cc, mincc, maxcc, level)

def todasLasCanciones(cc, mincc, maxcc, level):
    ## Recorrer las canciones
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
                print ("Nombre: {0:43s} Pack: {1:17s} Colección: {2:20s} Dificultad: {3:3s} Bando: {4:9s} Duración: {5:7s}"
                    .format(cancion, pack, coleccion, nivel, bando, duracion))
            i += 1
        if mincc < 8: mincc += 0.5
        else: mincc = round(mincc+0.1, 1)

def cancionesPorPack(cc, mincc, maxcc, level, pack):
    recorrer = True
    if level == 'byd':
        packsSindBYD = ["Sunset Radiance","Extend Archive","Ephemeral Page","Esoteric Order","Divided Heart","World Extend","Lasting Eden"]
        for i in packsSindBYD:
            if i == pack: 
                print(pack + " no tiene ninguna canción con dificultad beyond")
                recorrer = False
    ## Recorrer las canciones
    if recorrer:
        while mincc <= maxcc:
            i = 0
            for canciones in data['canciones']:
                if data['canciones'][i][cc] == mincc and data['canciones'][i]['pack'] == pack:
                    cancion = data['canciones'][i]['nombre']
                    coleccion = data['canciones'][i]['col']
                    if coleccion == None: coleccion = 'Ninguna'
                    nivel = data['canciones'][i][level]
                    bando = data['canciones'][i]['lado']
                    duracion = data['canciones'][i]['length']
                    print ("Nombre: {0:43s} Colección: {1:20s} Dificultad: {2:3s} Bando: {3:9s} Duración: {4:7s}"
                        .format(cancion, coleccion, nivel, bando, duracion))
                i += 1
            if mincc < 8: mincc += 0.5
            else: mincc = round(mincc+0.1, 1)

## Cojer el json de internet
try:
    file = requests.get('https://raw.githubusercontent.com/JavierEstudios/ritmo/main/canciones.json', timeout=1)
except:
    print("Error al coger los datos")
else:
    data = file.json()
    ## Llamar al resto del programa
    funcionPrincipal()
    file.close()
