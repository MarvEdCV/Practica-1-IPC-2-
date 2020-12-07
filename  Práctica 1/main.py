
import sys #Lo importo solamente para cerrar el programa
import json
#Variables globales
lines = []
line = []
recordList = []
lineSplit = []
idList=[]
placeList=[]

#Clase creada para poder manejar objetos de tipo Datos para cada registro diferente
class Data:
    def __init__(self,id,name,lastName,age,place,salary):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.age = age
        self.place = place
        self.salary = salary

#Creo funcion para limitar las opciones seleccionadas por el usuario, en cualquier menu.
def InvalidOp(op, limI, limS):
    if limI > op or op > limS:
        print("\nSu opcion esta fuera de los parametros, intente ingresar una opcion correcta\n")
    else:
        print("Opcion valida\n")

def ReadingData():
    global lines , line, recordList, lineSplit,idList
    nameFile =  input('Escriba la ruta o el nombre(como ruta relativa) del archivo csv debe de'
                      ' ingresar un nombre de ls siguiente manera(ejemplo.csv): \n')

    fileCSV = open(nameFile,'r',encoding='UTF-8')#Abro el archivo en modo lectura

    lines = fileCSV.readlines()#Guardo todas las lineas del CSV en un solo vector para luego manipularlo
    fileCSV.close()  # Cierro el archivo
    for line in lines:
        if line != lines[0]:
            lineSplit = line.split(",")
            if lineSplit[0] not in idList:
                idList.append(lineSplit[0])#Creo una lista de Id para filtrar luego los que se vayan añadiendo
                recordList.append(Data(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4], lineSplit[5]))
                # Aqui ya tengo una lista con todos los registros y sus debidos atributos
            elif (lineSplit[0] in idList):
                print("\nSe ha  encontrado un Id repetido!!!\n")
            if lineSplit[4] not in placeList:
                placeList.append(lineSplit[4])

    for printe in recordList:
        print(printe.id)
        print(printe.name)
        print(printe.lastName)
        print(printe.age)
        print(printe.place)
        print(printe.salary+'\n')
    print("\nArchivo CSV leído y procesado con éxito!!!\n")

def Calculations():

    promAge=0
    dictionary={}
    i=0
    for datos in recordList:
        cont = 0
        temporalPlace = datos.place
        for datos1 in recordList:
            if(datos1.place == temporalPlace):
                cont+=1
                promAge = promAge + float(datos1.age)
                print(cont)
    #dictionary = dictionary.update({temporalPlace: {'Cadidatos': cont, 'Edad Promedio': (promAge / cont)}})
    print(dictionary)
def MainMenu():
    op=0
    while op < 1 or op > 4:
        print('#####   Easy Solution - Procesamiento de datos   #####\n'
              '#####                Menú Principal              #####\n'
              '------------------------------------------------------\n'
              '#####   1)Lectura de archivo CSV                 #####\n'
              '#####   2)Cálculo de Datos                       #####\n'
              '#####   3)Generación de archivo JSON             #####\n'
              '#####   4)Cerrar programa                        #####\n')
        op = int(input('Seleccione la opcion deseada: '))
        InvalidOp(op,1,4)
        if op == 1:
            ReadingData()
            MainMenu()
        elif op == 2:
            Calculations()
            MainMenu()
        elif op == 3:
            print("tres")
            MainMenu()
        elif op == 4:
            sys.exit()
MainMenu()