# En mantenimiento

import psycopg2
import main_por_rol

host = '192.168.56.104'




def loginito(usuarito, contrasenyita):
    
    try:
        connexio = psycopg2.connect(
            dbname="hospital",
            user=usuarito,
            password=contrasenyita,
            host=host,
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
        host=host,
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
        print("| 1. Dar de baja un usuario existente    |")
        print("| 2. Consultar usuarios existentes       |")
        print("| 3. Crear Datos Dummy                   |")
    
    if rol == "medico":
        print("| 1. Consultar historial de un paciente  |")
        print("| 2. Horario del medico                  |")
        print("| 3. Consultar habitación de un paciente |")
        print("| 4. Operacions previstes                |")
        print("| 5. Consultar visitas planificadas      |")
        print("| 6. Aparatos medicos por quirofano      |")
        print("| 7. Consultar enfermedades más comunes  |")
   
    if rol == "enfermero":
        print("| 1. A que medic@ estas enlazad@         |")
        print("| 2. En que habitación está el paciente  |")
        print("| 3. Que medicación tiene el paciente    |")
        print("| 4. Operacions previstes                |")
        print("| 5. Aparatos medicos por quirofano      |")
    
    if rol == "celador":
        print("| 1. En que habitación está el paciente  |")
    
    if rol == "conductor_ambulancia":
        print("| 1. Consulta la habitación de salida    |")
    
    if rol == "administrador_hospital":
        print("| 1. Consultar el personal del hospital  |")
        print("| 2. Dar de alta a un nuevo trabajador   |")
        print("| 3. Exportar datos de las visitas       |")
        print("| 4. Consultar nombre de visites per dia |")
        print("| 5. Consultar medico más activo         |")
        print("| 6. Consultar enfermedades más comunes  |")
    
    if rol == "recepcionista":
        print("| 1. Dar de alta a un nuevo paciente     |")
        print("| 2. Consultar pacientes ingresados      |")
        print("| 3. Consultar habitaciones libres       |")
        print("| 4. Consultar habitaciones ocupadas     |")
        print("| 5. Consultar reservas de habitaciones  |")
        print("| 6. Consultar contenido de la planta    |")
    
    print("+----------------------------------------+")
    
    opcion = input("Introduce una opción: ")
    
    return opcion
    
def main_connexio():
    usuarito = input("Introduce el nombre de usuario: ")
    contrasenyita = input("Introduce la contraseña: ")
    if loginito(usuarito, contrasenyita) == True:
        print("+----------------------------------------+")
        print("|     Conexión establecida con éxito     |")
        print("+----------------------------------------+")
        rolecitos = enQueRolsitoEsta(usuarito)
        seguimos = True 
        while seguimos:
            opcion = int(menuPorRol(rolecitos))
            if rolecitos == 'administrador_informatico':
                main_por_rol.menuAdminInformatico(usuarito, contrasenyita, opcion)
            if rolecitos == 'medico':
                main_por_rol.menuMedico(usuarito, contrasenyita, opcion)
            if rolecitos == 'enfermero':
                main_por_rol.menuEnfermero(usuarito, contrasenyita, opcion)
            if rolecitos == 'celador':
                main_por_rol.menuCelador(usuarito, contrasenyita, opcion)
            if rolecitos == 'conductor_ambulancia':
                main_por_rol.menuConductorAmbulancia(usuarito, contrasenyita, opcion)
            if rolecitos == 'administrador_hospital':
                main_por_rol.menuAdminHospital(usuarito, contrasenyita, opcion)
            if rolecitos == 'recepcionista':
                main_por_rol.menuRecepcionista(usuarito, contrasenyita, opcion)
            if opcion == 0:
                seguimos = False     