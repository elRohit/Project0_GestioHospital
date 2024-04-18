# En mantenimiento

import psycopg2
    
def loginito(usuarito, contrasenyita):
    
    try:
        connexio = psycopg2.connect(
            dbname="hospital",
            user=usuarito,
            password=contrasenyita,
            host="10.94.255.129",
            port="5432",
            sslmode="require"
        )
        if connexio:
            return True
    except psycopg2.Error as e:
        print(f"Error en la conexión: {e}")
        return False
    finally:
        connexio.close()

def enQueRolsitoEsta(usuarito):
    
    connexio = psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="P@ssw0rd",
        host="10.94.255.129",
        port="5432",
        sslmode="require"
        )
    
    cur = connexio.cursor()
    SQLita = f"SELECT r.rolname AS usuario, r1.rolname AS rol FROM pg_catalog.pg_roles r JOIN pg_catalog.pg_auth_members m ON (m.member = r.oid) JOIN pg_roles r1 ON (m.roleid = r1.oid) WHERE r.rolcanlogin AND r.rolname = '{usuarito}' ORDER BY 1;"
    cur.execute(SQLita)
    resultadito = cur.fetchall()
    cur.close()
    connexio.close()
    rol = str(resultadito[0][1])
    return rol
    
def menuPorRol(rol):
    if rol == "administrador":
        print("+----------------------------------------+")
        print("| 1. Dar de alta un nuevo usuario        |")   
        print("| 2. Dar de baja un usuario existente    |")
        print("| 3. Dar de alta un nuevo paciente       |")
        print("| 4. Dar de baja un paciente existente   |")
        print("| 5. Consultar usuarios existentes       |")
        print("+----------------------------------------+")
    if rol == "medico":
        print("| 1. Consultar historial de un paciente  |")


def main_connexio():
    usuarito = input("Introduce el nombre de usuario: ")
    contrasenyita = input("Introduce la contraseña: ")
    if loginito(usuarito, contrasenyita) == True:
        print("+----------------------------+")
        print("Conexión establecida con éxito")
        rolecitos = enQueRolsitoEsta(usuarito)
        menuPorRol(rolecitos)
        
        
main_connexio()