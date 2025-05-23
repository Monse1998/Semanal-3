print("Bienvenidos al Gestor de Playlists del equipo 3")


playlists = {}

while True:
    print("\n1. Crear una playlist")
    print("2. Agregar canción a una playlist")
    print("3. Eliminar canción de una playlist")
    print("4. Modificar información de una canción")
    print("5. Consultar playlists")
    print("6. Salir")
    
    opcion = input("Opción: ")
    
    try:
        opcion = int(opcion)  
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue

# Opcion 1    
    if opcion == 1:
        while True:
            nombre_playlist = input("Ingresa el nombre de la nueva playlist: ")
            if nombre_playlist not in playlists:
                playlists[nombre_playlist] = set()
                print(f"Playlist '{nombre_playlist}' creada.")
            else:
                print(f"La playlist '{nombre_playlist}' ya existe.")
            
            a1 = input("¿Deseas agregar otra playlist? \n1. Sí\n2. No\nOpción: ")
            if a1 == '2':
                print("Regresando al menú principal.")
                break

# Opcion 2    
    elif opcion == 2:
        while True:
            playlist = input("¿A qué playlist deseas agregar una canción? ")
            if playlist in playlists:
                cancion = input("¿Qué canción deseas agregar? ")
                playlists[playlist].add(cancion)
                print(f"La canción '{cancion}' ha sido agregada a la playlist '{playlist}'.")
            else:
                print(f"No existe la playlist '{playlist}'.")
            
            a1 = input("¿Deseas agregar otra canción? \n1. Sí\n2. No\nOpción: ")
            if a1 == '2':
                print("Regresando al menú principal.")
                break

# Opcion 3    
    elif opcion == 3:
        while True:
            playlist = input("¿De qué playlist deseas eliminar una canción? ")
            if playlist in playlists:
                cancion = input("¿Qué canción deseas eliminar? ")
                if cancion in playlists[playlist]:
                    playlists[playlist].remove(cancion)
                    print(f"La canción '{cancion}' ha sido eliminada de la playlist '{playlist}'.")
                else:
                    print(f"La canción '{cancion}' no está en la playlist '{playlist}'.")
            else:
                print(f"No existe la playlist '{playlist}'.")
            
            a1 = input("¿Deseas eliminar otra canción? \n1. Sí\n2. No\nOpción: ")
            if a1 == '2':
                print("Regresando al menú principal.")
                break

# Opcion 4    
    elif opcion == 4:
        while True:
            playlist = input("¿De qué playlist deseas modificar una canción? ")
            if playlist in playlists:
                cancion_actual = input("¿Qué canción deseas modificar? ")
                if cancion_actual in playlists[playlist]:
                    nueva_cancion = input(f"Ingresa el nuevo nombre para '{cancion_actual}': ")
                    playlists[playlist].remove(cancion_actual)
                    playlists[playlist].add(nueva_cancion)
                    print(f"La canción '{cancion_actual}' ha sido cambiada por '{nueva_cancion}' en la playlist '{playlist}'.")
                else:
                    print(f"La canción '{cancion_actual}' no está en la playlist '{playlist}'.")
            else:
                print(f"No existe la playlist '{playlist}'.")
            
            a1 = input("¿Deseas modificar otra canción? \n1. Sí\n2. No\nOpción: ")
            if a1 == '2':
                print("Regresando al menú principal.")
                break

# Opcion 5    
    elif opcion == 5:
        while True:
            if playlists:
                print("\nPlaylists y sus canciones:")
                for playlist, canciones in playlists.items():
                    print(f"Playlist: {playlist}")
                    if canciones:
                        print("  Canciones:", ', '.join(canciones))
                    else:
                        print("  No hay canciones en esta playlist.")
            else:
                print("No tienes playlists creadas.")
            
            a1 = input("¿Deseas consultar nuevamente? \n1. Sí\n2. No\nOpción: ")
            if a1 == '2':
                print("Regresando al menú principal.")
                break
            
# Opcion 6    
    elif opcion == 6:
        print("Hasta la próxima...")
        break
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")