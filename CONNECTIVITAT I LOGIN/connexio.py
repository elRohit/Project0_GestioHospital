import psycopg2

usuarito = input("Introduce el nombre de usuario: ")
contrasenya = input("Introduce la contraseña: ")


def loginito(usuarito, contrasenya):
    try:
        connexio = psycopg2.connect(
            dbname="hospitalito",
            user=usuarito,
            password=contrasenya,
            host="192.168.56.120",
            port="5432"
        )
        return connexio
    except psycopg2.Error as e:
        print(f"Error en la conexión: {e}")
        return None
    
def queryta():
    print("+----------------------------+")
    print("Conexión establecida con éxito")
    print("+----------------------------+")
    print("______Que desea hacer?________")
    print()
    pass

if loginito(usuarito, contrasenya) == True:
    queryta()
else:
    print("Error en la conexión")
    