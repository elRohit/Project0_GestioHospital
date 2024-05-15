# Bloc de Programació

## Índex de continguts

1. [Codi de Programació (engloba tots els apartats de PRG)](#Codi-de-programació).
2. Processos, Funcions i Triggers.
3. Exportació de dades.

## Codi de Programació.
### Codi de connectivitat i login
```
import psycopg2
import main_por_rol

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
```

En aquest codi fa de definició del inici de sessió amb l'usuari a la base de dades. Ja que com tenim 5 codis de Python, aquest fa com definició de login.
Depenent del rol que tinguis com usuari et sortirà un main diferent.

Després d'aquest codi formem els mains que corresponen a cada rol. Però abans de això comprovem quin rol té d'aquesta forma.
```
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
```
Amb aquesta definició i execució d'SQL podem veure el rol de l'usuari amb el qual hem fet login.

Ara finalment fem un print de cada main.
```
def menuPorRol(rol):
    print("+----------------------------------------+")
    print("| 0. Salir                               |")
    
    if rol == "administrador_informatico":
        print("| 1. Dar de baja un usuario existente    |")
        print("| 2. Consultar usuarios existentes       |")
    
    if rol == "medico":
        print("| 1. Consultar historial de un paciente  |")
        print("| 2. Consultar medicación de un paciente |")
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
        print("| 3. Dar de baja a un trabajador         |")
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
```
