import psycopg2

usuarito = input("Introduce el nombre de usuario: ")
contrasenya = input("Introduce la contraseña: ")


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
    mainPermisitos(permisitos())

def permisitos(usuarito):
    
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user="postgres",
        password="P@ssw0rd",
        host="10.94.255.109",
        port="5432"
        )
    
    listitaPermisitos = []
    
    SQLita = f"SELECT table_schema, table_name, privilege_type, is_grantablee FROM information_schema.table_privileges WHERE grantee = {usuarito} AND is_grantablee = 'YES';"
    cur = connexio.cursor()
    cur.execute(SQLita)
    rows = cur.fetchall()
    
    for row in rows:
        listitaPermisitos.append(row[2])
        
    cur.close()
    connexio.close()
    
    return listitaPermisitos

def mainPermisitos(listitaPermisitos:list):
    if listitaPermisitos(usuarito) == []:
        print("No tiene permisos")
    else:
        for permisito in listitaPermisitos:
            print(permisito)
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
    loginito(usuarito, contrasenya)
    
    if loginito(usuarito, contrasenya) == True:
        permisitos()
        mainQueryta()
    else:
        pass
        
main()
    