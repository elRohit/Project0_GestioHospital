import psycopg2
    
def loginito(usuarito, contrasenyita):
    
    try:
        connexio = psycopg2.connect(
            dbname="hospitalito",
            user=usuarito,
            password=contrasenyita,
            host="10.94.255.109",
            port="5432"
        )
        if connexio:
            return True
    except psycopg2.Error as e:
        print(f"Error en la conexión: {e}")
        return False
    
def mainQueryta(usuarito, tablitaAfectadita):
    print("+----------------------------+")
    print("|      ¿Que desea hacer?     |")
    print("+----------------------------+")
    permisitos(usuarito, tablitaAfectadita)
    print("+----------------------------+")

def permisitos(usuarito, tablitaAfectadita):
    
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user="postgres",
        password="P@ssw0rd",
        host="10.94.255.109",
        port="5432"
        )
    
    SQLita = f"SELECT privilege_type FROM information_schema.table_privileges WHERE grantee = '{usuarito}' AND is_grantable = 'YES' AND table_catalog = 'hospitalito' AND table_name = '{tablitaAfectadita}';"
    cur = connexio.cursor()
    cur.execute(SQLita)
    rows = cur.fetchall()
    cur.close()
    connexio.close()
     
    for row in rows:
        if row == ('INSERT',):
            print(f"{"1.- Insertar datos":<29}|")
        elif row == ('SELECT',):
            print(f"{"2.- Consultar datos":<29}|")
        elif row == ('UPDATE',):
            print(f"{"3.- Actualizar datos":<29}|")
        elif row == ('DELETE',):
            print(f"{"4.- Borrar datos":<29}|")
        elif row == ('REFERENCES',):
            print(f"{"5.- Referenciar datos":<29}|")
        elif row == ('TRIGGER',):
            print(f"{"6.- Crear triggers":<29}|")

def insertarDatitos(usuarito,contrasenyita, tablitaAfectadita):
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user=usuarito,
        password=contrasenyita,
        host="10.94.255.109",
        port="5432"
    )
    cur = connexio.cursor()
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tablitaAfectadita}';")
        
    listitaAnyaditos = []
    rows = cur.fetchall()
    for row in rows:
        listitaAnyaditos.append(input(f"Introduce el valor de {row[0]}: "))
            
    cur.execute(f"INSERT INTO {tablitaAfectadita} VALUES {tuple(listitaAnyaditos)};")
    print("Datos insertados correctamente")
    print(f"Has insertado los siguientes datos: {listitaAnyaditos}")
    connexio.commit()
        
    cur.close()
    connexio.close()
        
def consultarDatitos(usuarito,contrasenyita, tablitaAfectadita):
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user=usuarito,
        password=contrasenyita,
        host="10.94.255.109",
        port="5432"
    )
    cur = connexio.cursor()
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tablitaAfectadita}';")
        
    print("Los campos de la tabla son: ")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
            
    tuConsultitaCampitos = input("Introduce los campos que deseas realizar (separalos con ','): ").split(",")
        
    quiereCondicioncita = input("¿Desea añadir una condición? (s/n): ")
    if quiereCondicioncita.lower() == "s":
        condicioncita = input("Introduce la condición/es (ponga <campo> = <condición> <AND> ...): ")
            
    quiereOrdencito = input("¿Desea ordenar los datos? (s/n): ")
    if quiereOrdencito.lower() == "s":
        ordencito = input("Introduce el campo de orden y si es ascendente/descendente (ponga <campo> ASC/DESC):")
        
    if quiereCondicioncita == "s" and quiereOrdencito == "s":
        cur.execute(f"SELECT {','.join(tuConsultitaCampitos)} FROM {tablitaAfectadita} WHERE {condicioncita} ORDER BY {ordencito};")
            
    elif quiereCondicioncita == "s" and quiereOrdencito == "n":
        cur.execute(f"SELECT {','.join(tuConsultitaCampitos)} FROM {tablitaAfectadita} WHERE {condicioncita};")
            
    elif quiereCondicioncita == "n" and quiereOrdencito == "s":
        cur.execute(f"SELECT {','.join(tuConsultitaCampitos)} FROM {tablitaAfectadita} ORDER BY {ordencito};")
            
    elif quiereCondicioncita == "n" and quiereOrdencito == "n":
        cur.execute(f"SELECT {','.join(tuConsultitaCampitos)} FROM {tablitaAfectadita};")
    connexio.commit()
        
    rows = cur.fetchall()
    for row in rows:
        print(row)        
       
    cur.close()
    connexio.close()
 
def actualizarDatitos(usuarito,contrasenyita, tablitaAfectadita): 
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user=usuarito,
        password=contrasenyita,
        host="10.94.255.109",
        port="5432"
    )
    cur = connexio.cursor()
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tablitaAfectadita}';")
    
    print("Los campos de la tabla son: ")
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
    
    eleccionita = input("Introduce los campos que desea modificar (separelos con ','): ").split(",")
    condiciones = input("Introduce la condición campo = condicion (separelos con AND si es más de una condición): ").split("AND")
    
    for i in range(len(condiciones)):
        condiciones[i] = condiciones[i].strip()
    
    print(condiciones)
    
    print("Introduce los nuevos valores (separelos con ',' y en orden): ")
    nuevosValores = input().split(",") 
    
    for i in range(len(nuevosValores)):
        nuevosValores[i] = nuevosValores[i].strip()
        
    print(nuevosValores)
    
    cur.execute(f"UPDATE {tablitaAfectadita} SET {','.join(eleccionita)} = {tuple(nuevosValores)} WHERE {' AND '.join(condiciones)};")
        
    cur.close()
    connexio.close()
    

def queQuiereHacerito(usuarito,contrasenyita, eleccionita, tablitaAfectadita):
    
    if eleccionita == 1:
        insertarDatitos(usuarito,contrasenyita, tablitaAfectadita)
            
    elif eleccionita == 2:
        consultarDatitos(usuarito,contrasenyita, tablitaAfectadita)
        
    elif eleccionita == 3:
        actualizarDatitos(usuarito,contrasenyita, tablitaAfectadita)
    elif eleccionita == 4:
        pass
    elif eleccionita == 5:
        pass
    elif eleccionita == 6:
        pass


def main_connexio():
    usuarito = input("Introduce el nombre de usuario: ")
    contrasenyita = input("Introduce la contraseña: ")
    tablitaAfectadita = input("Introduce la tabla a la cual quiere efectuar un comando: ")
    if loginito(usuarito, contrasenyita) == True:
        print("+----------------------------+")
        print("Conexión establecida con éxito")
        prosigamitos = True
        while prosigamitos == True:
            mainQueryta(usuarito, tablitaAfectadita)
            eleccionita = int(input("Introduce el número de la acción: "))
            queQuiereHacerito(usuarito, contrasenyita, eleccionita, tablitaAfectadita)
            quiereContinuaarito = input("¿Desea continuar? (s/n): ")
            if quiereContinuaarito.lower() == "n":
                prosigamitos = False
    
main_connexio()