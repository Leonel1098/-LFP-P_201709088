from tkinter import filedialog
from tkinter import Tk
from Pelicula import *
from graphviz import Digraph
lista_peliculas = []

def CargarArchivo():
    
    try:
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        #Abre Ventana para Buscar el archivo .lfp 
        archivo =  filedialog.askopenfilename() 
        print("Archivo Seleccionado", archivo)

        #Abre el achivo 
        archivo_texto = open(archivo ,'r',encoding="utf8")
        #print(archivo_texto)
        #print("muestra1")

        #Contenido del archivo leido 
        texto = archivo_texto.read()
        #print(texto)
        global datos
        datos = texto
        root.destroy()
        #diccionario()
        #mostrarPeliculas()
    except FileNotFoundError:
        print("El archivo no se cargó correctamente, vuelva a intentarlo.")


 #Agrega la información del archivo en un diccionario para poder manejar las peliculas por separado       
def diccionario():
    info = datos.split("\n")
    for s in info:
        diccionario = s.split(";")

        peli = {
            "nombre:" +diccionario[0],
            "reparto:" +diccionario[1],
            "año:" +diccionario[2],
            "genero:"+diccionario[3]
        }
        lista_peliculas.append(peli)
    print(lista_peliculas)

#Muestra las películas cargadas en el diccionario por el archivo 
def mostrarPeliculas():
    #print(lista_peliculas)
    info = datos.split("\n")
# con un for itero la cadena de texto y hago que guarde en una posición diferente de la lista la información cada que encuentre un ";"
    for i in info:
        diccionario = i.split(";")
        print("------------------Película-----------------")
        print("Nombre:"+diccionario[0])
        print("Reparto:"+diccionario[1])
        print("Año:"+diccionario[2])
        print("Género:"+diccionario[3])

def mostrarActores():
    info = datos.split("\n")

    # Aquí agrego un indice a cada pelicula que se agrega al diccionario con la funcion enumerate para poder seleccionar la película.
    for i, nombre_peli in enumerate(info, start=1):
            pelicula = nombre_peli.split(";")[0]
            print(i,"Nombre de Películas: "+ pelicula )
    entrada = int(input("Seleccione una película para mostrar a sus actores..."))
    
    # Se valida que la opción del usuario sea correcta y se seleccionan los actores de la película elegida
    if 1 <= entrada <= len(info):
        actores = info[entrada-1].split(";")[1]
        print("\n Los actores de la película seleccionada son: " + actores)
    else:
        print("Ingrese una  opción válida")

def filtrarActor():
    entrada_actor = input("Ingrese el Nombre del Actor:... ")
    actor_de_pelicula = []

    for pelicula in datos.split("\n"):
        datos_pelicula = pelicula.split(';')
        actores = datos_pelicula[1].split(',')

        if entrada_actor in actores:
            actor_de_pelicula.append(datos_pelicula[0])

    if actor_de_pelicula:
        print("Las películas en las que está " + entrada_actor + " son:...")
        for pelicula in actor_de_pelicula:
            print(pelicula)
    else:
        print("No se encontraron películas en las que esté" + entrada_actor)


def filtrarAño():
    entrada_anio= input("Ingrese el año de la película:...")
    anio_pelicula = []

    for pelicula in datos.split("\n"):
        datos_pelicula = pelicula.split(";")
        anios = datos_pelicula[2]

        if entrada_anio in anios:
            anio_pelicula.append((datos_pelicula[0],datos_pelicula[3]))
    
    if anio_pelicula:
        print("Las películas para el año ingresado son:... ")
        for pelicula in anio_pelicula:
            print("\n Nombre: "+pelicula[0]+", Género: "+pelicula[1])
    else:
        print("No se encontraron películas para el año ingresado, ingrese un año válido.")


def filtrarGenero():
    entrada_genero= input("Ingrese el género de la película:...")
    genero_pelicula = []

    for pelicula in datos.split("\n"):
        datos_pelicula = pelicula.split(";")
        generos = datos_pelicula[3]

        if entrada_genero in generos:
            genero_pelicula.append(datos_pelicula[0])
    
    if genero_pelicula:
        print("Las películas para el genero ingresado son:... ")
        for pelicula in genero_pelicula:
            print( "Nombre: "+pelicula)
    else:
        print("No se encontraron películas para el género ingresado, ingrese un género válido.")




def grafica():
    info = datos.split("\n")

    lista_actores = {}
    for pelicula_info in info:
        # Dividir la información de la película por ';'
        datos_pelicula = pelicula_info.split(';')
        nombre_pelicula = datos_pelicula[0]
        actores = datos_pelicula[1].split(',')
        año = datos_pelicula[2]
        genero = datos_pelicula[3]
        for actor in actores:
            actor = actor.strip()
            if actor not in lista_actores:
                lista_actores[actor] = []
            lista_actores[actor].append((nombre_pelicula, año, genero))
                    
    graph = Digraph()

    for actor, peliculas in lista_actores.items():
        graph.node(actor, shape="circle", style = "filled", fillcolor="blue", color = "skyblue")
        for pelicula in peliculas:
            nombre_pelicula = f"{pelicula[0]} ({pelicula[1]}) - {pelicula[2]}"  
            graph.node(nombre_pelicula, shape="circle", style = "filled", fillcolor="orange", color = "skyblue")

    for actor, peliculas in lista_actores.items():
        for pelicula in peliculas:
            nombre_pelicula = f"{pelicula[0]} ({pelicula[1]}) - {pelicula[2]}"
        
            graph.edge(actor, nombre_pelicula)

    graph.attr(rankdir='LR')
    graph.render("Gráfica", format="pdf", cleanup=True)

    print("Gráfica creada como 'Gráfica.pdf'")




def MenuFiltrar():
     while True:
        print("")
        print(".............MENÚ FILTRAR.............")
        print("     1. Filtrar por Actor")
        print("     2. Filtrar por Año")
        print("     3. Filtrar por Género")
        print("     4. Regresar a Menú ")
        print("")
        # solicitamos una opción al usuario
        opcionMenu = input(" Por favor seleccione una opcion >> ")
        
        if opcionMenu =="1":
           print("  ---->Filtrar por Actor")
           print("")
           filtrarActor()

        elif opcionMenu =="2":
            print(" ---->Filtrar por Año")
            print("")
            filtrarAño()

        elif opcionMenu =="3":
            print(" ---->Filtrar por Género")
            print("")
            filtrarGenero()
        elif opcionMenu=="4":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")



def MenuGestionar():
     while True:
        print("")
        print(".............MENÚ GESTIONAR.............")
        print("     1. Mostrar Películas")
        print("     2. Mostrar Actores")
        print("     3. Regresar a Menú")
        print("")
        # solicituamos una opción al usuario
        opcionMenu = input(" Por favor seleccione una opcion >> ")
        
        if opcionMenu =="1":
           print("  ---->Mostrar Películas")
           print("")
           mostrarPeliculas()
        elif opcionMenu =="2":
            print(" ---->Mostar Actores")
            print("")
            mostrarActores()
            
        elif opcionMenu=="3":
            break
            
        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")

def Menu():
    print("\n--Lenguajes Formales y de Programación \n--Sección B+ \n--201709088 \n--Leonel Antonio González García")
    input("Presione una tecla para continuar...")
    while True:
        print("\n******************************")
        print("----------Menú----------")
        print("1. Cargar Archivo de Entrada")
        print("2. Gestionar Peliculas")
        print("3. Filtrado")
        print("4. Gráfica")
        print("5. Salir")
        
        opcion = input("Por favor seleccione una opción del Menú...")
        

        if opcion == "1":
            print("")
            CargarArchivo()
            print("Archivo cargado con éxito")

        elif opcion == "2":
            MenuGestionar()
            print("Gestión completa")

        elif opcion == "3":
            MenuFiltrar()
            print("Filtrado completo")

        elif opcion == "4":
            grafica()
            print("Grafica completa")

        elif opcion == "5":
            print("Gracias por visitarnos :) ")
            break

        else:
            print("Por favor ingrese una opción válida...")

Menu()