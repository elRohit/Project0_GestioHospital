import manipulacion_dummy as backend

# Def Menu Principal
def main():
    try:
        loop_breaker = True
        while loop_breaker:
            print("+---------------------------------------------+")
            print(" Bienvenido/a al Hospitalito IRA              |")
            print("+---------------------------------------------+")
            print("¿Qué desea hacer?                             |")
            print("1.- Rellenar la base de datos                 |")
            print("2.- vaciar la base de datos                   |")
            print("3.- Crear los indices                         |")
            print("4.- Salir                                     |")
            print("+---------------------------------------------+")
            eleccionita = int(input("Introduce el número de la opción: "))

            if eleccionita == 1:
                backend.creacion()
            elif eleccionita == 2:
                backend.clean_all()
            elif eleccionita == 3:
                backend.indexos()
            elif eleccionita == 4:
                print("Cargando ==> Saliendo del programa...Hasta la próxima!")
                loop_breaker = False
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
