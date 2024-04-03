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
    pass

def permisitos(usuarito):
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user="postgres",
        password="P@ssw0rd",
        host="192.168.56.120",
        port="5432"
        )
    SQLita = f"SELECT * FROM information_schema.table_privileges WHERE grantee = {usuarito}"
    cur = connexio.cursor()
    cur.execute(SQLita)
    listitaPermisitos = []
    rows = cur.fetchall()
    for row in rows:
        listitaPermisitos.append(row)
    cur.close()
    connexio.close()
    return listitaPermisitos

if loginito(usuarito, contrasenya) == True:
    permisitos()
    queryta()
else:
    print("Error en la conexión")
    