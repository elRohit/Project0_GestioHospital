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
    print("+----------------------------------------+")
    print("| 0. Salir                               |")
    
    if rol == "administrador_informatico":
        print("| 1. Dar de alta un nuevo usuario        |")   
        print("| 2. Dar de baja un usuario existente    |")
        print("| 3. Dar de alta un nuevo paciente       |")
        print("| 4. Dar de baja un paciente existente   |")
        print("| 5. Consultar usuarios existentes       |")
    
    if rol == "medico":
        print("| 1. Consultar historial de un paciente  |")
        print("| 2. Consultar medicación de un paciente |")
        print("| 3. Consultar habitación de un paciente |")
   
    if rol == "enfermero":
        print("| 1. A que medic@ estas enlazad@         |")
        print("| 2. En que habitación está el paciente  |")
        print("| 3. Que medicación tiene el paciente    |")
    
    if rol == "celador":
        print("| 1. En que habitación está el paciente  |")
    
    if rol == "conductor_ambulancia":
        print("| 1. En que habitación está el paciente  |")
        print("| 2. Que habitaciones están libres       |")
        print("| 3. Que habitaciones están ocupadas     |")
    
    if rol == "administrador_hospital":
        print("| 1. Consultar el personal del hospital  |")
        print("| 2. Dar de alta a un nuevo usuario      |")
        print("| 3. Dar de baja a un usuario existente  |")
    
    if rol == "recepcionista":
        print("| 1. Dar de alta a un nuevo paciente     |")
        print("| 2. Consultar pacientes ingresados      |")
        print("| 3. Consultar habitaciones sin reserva  |")
        print("| 4. Consultar habitaciones reservadas   |")
    
    print("+----------------------------------------+")
    
    opcion = input("Introduce una opción: ")
    
    return opcion
    
    
    
def menuAdminInformatico(usuarito, contrasenyita, opcion):
    if opcion == 1:
        try:
            usuaritoCreado = input("Introduce el nombre de usuario: ")
            contrasenyitaCreada = input("Introduce la contraseña: ")
            print("Ahora debera elegir el rol del usuario. ")
            print("Tiene estas opciones: ")
            print("administrador_informatico, medico, enfermero, celador,")
            print("conductor_ambulancia, administrador_hospital, recepcionista, invitado.")
            rolcitoCrear = input("Introduce su rama profesional (rol): ")
            SQLita = f"CREATE ROLE {usuaritoCreado} LOGIN PASSWORD '{contrasenyitaCreada}' IN ROLE {rolcitoCrear};"
            connexio = psycopg2.connect(
                dbname="hospital",
                user=usuarito,
                password=contrasenyita,
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            cur = connexio.cursor()
            cur.execute(SQLita)
            connexio.commit()
            cur.close()
            connexio.close()
        
            print(" Su usuario ha sido creado con éxito. ")  
        except psycopg2.Error as e:
            
            print("El usuario no ha podido ser creado. Puede ser que exista un usuario con el mismo nombre.")
        
    if opcion == 2:
            
            usuaritoBorrado = input("Introduce el nombre de usuario a borrar: ")
            estaSeguro = input("¿Estás seguro de que quieres borrar el usuario? (s/n): ")
            SQLita = f"DROP ROLE {usuaritoBorrado};"
                        
            if estaSeguro == "s":
                try:
                    connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                    )
                    cur = connexio.cursor()
                    cur.execute(SQLita)
                    connexio.commit()
                    cur.close()
                    connexio.close()    
                    print("El usuario ha sido borrado con éxito.")
                
                except psycopg2.Error as e:
                    print("Error al borrar el usuario.")          
            else:
                print("El usuario no ha sido borrado.")
            
    if opcion == 3:
        pass
    if opcion == 4:
        pass
    if opcion == 5:
        pass
    
def menuMedico(usuarito, contrasenyita, opcion):
    if opcion == 1:
        pass
    if opcion == 2:
        pass
    if opcion == 3:
        pass
    
def main_connexio():
    usuarito = input("Introduce el nombre de usuario: ")
    contrasenyita = input("Introduce la contraseña: ")
    if loginito(usuarito, contrasenyita) == True:
        print("+----------------------------------------+")
        print("|     Conexión establecida con éxito     |")
        print("+----------------------------------------+")
        rolecitos = enQueRolsitoEsta(usuarito)
        opcion = menuPorRol(rolecitos)
        if rolecitos == "administrador_informatico":
            menuAdminInformatico(usuarito, contrasenyita, opcion)
        
        
main_connexio()