import connexio_login
import create_user


def main():
    print("+-------------------------------+")
    print(" Bienvenido/a al Hospitalito IRA")
    print("+-------------------------------+")
    print("¿Qué desea hacer?               |")
    print("1.- Iniciar sesión              |")
    print("2.- Registrate                  |")
    print("3.- Salir                       |")
    print("+-------------------------------+--+")
    eleccionita = int(input("Introduce el número de la opción: "))
    while eleccionita != 3:
        print("+-------------------------------+--+")
        if eleccionita == 1:
            connexio_login.main_connexio()
        elif eleccionita == 2:
            create_user.main_inserir_usuarito()
        print("+-------------------------------+")
        print("¿Qué desea hacer?               |")
        print("1.- Iniciar sesión              |")
        print("2.- Registrate                  |")
        print("3.- Salir                       |")
        print("+-------------------------------+--+")
        eleccionita = int(input("Introduce el número de la opción: "))
    if eleccionita == 3:
            print("Hasta la próxima")
        
main()