import manipulacion_dummy as backend


def main():
    loop_breaker = True
    while system_breaker:
        print("+---------------------------------------------+")
        print(" Bienvenido/a al Hospitalito IRA              |")
        print("+-------------------------------+")
        print("¿Qué desea hacer?                             |")
        print("1.- Rellenar la base de datos                 |")
        print("2.- vaciar la base de datos                   |")
        print("3.- Salir                                     |")
        print("+---------------------------------------------+")
        eleccionita = int(input("Introduce el número de la opción: "))
        
        if eleccionita == 1:
            backend.creacion()
        elif eleccionita == 2:
            backend.eliminar_db_content()
        elif eleccionita == 3:
            print("Hasta la próxima")
            loop_breaker = False
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        
if __name__ == "__main__":
    main()
