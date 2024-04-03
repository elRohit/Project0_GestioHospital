import psycopg2

usuarito = input("Introduce el nombre de usuario: ")
contrasenya = input("Introduce la contraseña: ")
tablaAfectada = input("Introduce la tabla a la cual quiere efectuar un comando: ")


def loginito(usuarito, contrasenya):
    try:
        connexio = psycopg2.connect(
            dbname="hospitalito",
            user=usuarito,
            password=contrasenya,
            host="10.94.255.109",
            port="5432"
        )
        if connexio:
            return True
    except psycopg2.Error as e:
        print(f"Error en la conexión: {e}")
        return False
    
def mainQueryta():
    print("+----------------------------+")
    print("Conexión establecida con éxito")
    print("+----------------------------+")
    print("______¿Que desea hacer?_______")
    permisitos(usuarito, tablaAfectada)

def permisitos(usuarito, tablaAfectada):
    
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user="postgres",
        password="P@ssw0rd",
        host="10.94.255.109",
        port="5432"
        )
    
    listitaPermisitos = []
    SQLita = f"SELECT privilege_type FROM information_schema.table_privileges WHERE grantee = '{usuarito}' AND is_grantable = 'YES' AND table_catalog = 'hospitalito' AND table_name = '{tablaAfectada}';"
    cur = connexio.cursor()
    cur.execute(SQLita)
    rows = cur.fetchall()
    
    for row in rows:
        listitaPermisitos.append(row)
        
    cur.close()
    connexio.close()
     
    if listitaPermisitos == []:
        print("No tiene permisos")
    else:
        for permisito in listitaPermisitos:
            if permisito == "SELECT":
                print("1. ¿Que quiere consultar?")
            elif permisito == "INSERT":
                print("2. ¿Que quiere insertar?")
            elif permisito == "UPDATE":
                print("3. ¿Que quiere actualizar?")
            elif permisito == "DELETE":
                print("4. ¿Que quiere borrar?")
            elif permisito == "TRUNCATE":
                print("5. ¿Que quiere truncar?")
                
def main():
    if loginito(usuarito, contrasenya) == True:
        mainQueryta()
    else:
        print("Error en la conexión")
        
main()
    