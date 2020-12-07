
import sys #Lo importo solamente para cerrar el programa
import json
#Variables globales
lines = []
line = []
recordList = []
lineSplit = []
idList=[]
placeList=[]
datass = {}

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

#Función para leer todos los datos del CSV y distribuirlos en una lista de objetos de tipo DATA con los atributos creados anteriormente
def ReadingData():
    global lines , line, recordList, lineSplit,idList
    contador=0
    nameFile =  input('Escriba la ruta o el nombre(como ruta relativa) del archivo csv debe de'
                      ' ingresar un nombre de ls siguiente manera(ejemplo.csv): \n')
    trucado = nameFile.split(".")
    if trucado[1] == 'CSV' or trucado[1] == 'csv':
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
                    contador+=1
                if lineSplit[4] not in placeList:
                    placeList.append(lineSplit[4])
        if contador > 0:
            print("\nSe ha  encontrado Id(s) repetido(s)!!! TOTAL= " + str(contador))
        print("\nArchivo CSV leído procesado y filtrado con éxito!!!\n")
    elif trucado[1] != "CSV" or trucado[1] != "csv" or trucado[1] != " ":
        print("\nEl archivo que estas tratando de ingresar no es CSV\n")

def conectDictionary(list): #Creo una función a la cual le paso una lista de diccionarios para unirlos en un solo diccionario

    dictionarys = {}

    for d in list:
        dictionarys.update(d)
    return dictionarys

def Calculations():
    if len(recordList) == 0:
        print("No se ha ingresado ningun registro de archivo CSV\n")
    elif len(recordList)>0:
        dictionary={}
        global datass
        temporalList=[]
        list = []
        for datos in placeList:
            cont = 0
            promAge=0
            promSalary=0
            temporalPlace = datos
            for datos1 in recordList:
                if(datos1.place == temporalPlace) and (temporalPlace not in temporalList):
                    cont+=1
                    promAge = promAge + float(datos1.age)
                    promSalary = promSalary + float(datos1.salary)
                    dictionary = {temporalPlace: {'Candidatos': cont, 'Edad Promedio': (promAge / cont),'Pretensión Salarial Promedio': (promSalary / cont)}}
                    list.append(dictionary)
            temporalList.append(temporalPlace)
            datass = conectDictionary(list)
        print("\nCalculos realizados correctamente, ya puede generar archivo Json!!!\n")
def generateJson():
    with open('Datos Procesados.json','w',encoding="utf-8") as f:
        json.dump(datass,f, ensure_ascii= False,indent=4)
    print("\nArchivo Json creado con éxito!!!\n")
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
            generateJson()
            MainMenu()
        elif op == 4:
            sys.exit()
MainMenu()