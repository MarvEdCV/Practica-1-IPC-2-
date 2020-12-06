
import sys #Lo importo solamente para cerrar el programa

#Variables globales
lines = []
line = []
recordList = []
lineSplit = []

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
    global lines , line, recordList, lineSplit
    nameFile =  input('Escriba la ruta o el nombre(como ruta relativa) del archivo csv debe de'
                      ' ingresar un nombre de ls siguiente manera(ejemplo.csv): \n')

    fileCSV = open(nameFile,'r',encoding='UTF-8')#Abro el archivo en modo lectura

    lines = fileCSV.readlines()#Guardo todas las lineas del CSV en un solo vector para luego manipularlo
    fileCSV.close()  # Cierro el archivo
    for line in lines:
        if line != lines[0]:
            lineSplit = line.split(",")
            recordList.append(Data(lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3],lineSplit[4],lineSplit[5]))
            #Aqui ya tengo una lista con todos los registros y sus debidos atributos.

    print("\nArchivo CSV leído y procesado con éxito!!!\n")

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
            print("dos")
            MainMenu()
        elif op == 3:
            print("tres")
            MainMenu()
        elif op == 4:
            sys.exit()
MainMenu()