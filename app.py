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
        print("******************************")
        opcion = input("Por favor seleccione una opción del Menú...")
        

        if opcion == "1":
            print("Archivo cargado con éxito")

        elif opcion == "2":
            print("Gestión completa")

        elif opcion == "3":
            print("Filtrado completo")

        elif opcion == "4":
            print("Grafica completa")

        elif opcion == "5":
            print("Gracias por visitarnos :) ")
            break

        else:
            print("Por favor ingrese una opción válida...")

Menu()