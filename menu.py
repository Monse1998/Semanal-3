print("Bienvenidos al Gestor de Playlists")
lista=[]
while True:
    print("1. Crear una playlist")
    print("2. Agregar canación a una playlist")
    print("3. Eliminiar canción")
    print("4. Modificar informacion de una canción")
    print("5. Consultar playlists ")
    print("6. Salir")
    opcion = input("Opción: ")
    
    try:
        opcion = int(opcion)  # Casting de string a entero
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue
    
    if opcion == 1:
        valor1 = input(f"Ingresa el nombre de la nueva playlist")
        lista.append(valor1)
        print(f"{lista}")
        
    elif opcion == 2:
        valor2 = input(f" ¿Que cancion desas agregar?  ")
    
    elif opcion == 3:
        valor3 = input(f" ¿Que cancion deseas elmininar?  ")
        
    elif opcion == 4:
        valor4=print(f"¿Que cancion deseas modificar?  ")
    
    if opcion == 5:
        valor5 = input(f"¿Que playlists deseas ver?  ")
        
    elif opcion == 6:
        valor6 = input(f" Hasta la otra...")
    break
else:
        print("Opción no válida. Inténtalo de nuevo.")