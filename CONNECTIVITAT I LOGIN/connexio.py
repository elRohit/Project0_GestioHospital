import psycopg2

usuarito = input("Introduce el nombre de usuario: ")
contrasenyita = input("Introduce la contraseña: ")
tablitaAfectadita = input("Introduce la tabla a la cual quiere efectuar un comando: ")
print("+----------------------------+")
print("Conexión establecida con éxito")


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
    
def mainQueryta():
    
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

def queQuiereHacerito(usuarito,contrasenyita, eleccionita, tablitaAfectadita):
    
    if eleccionita == 1:
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
            
    elif eleccionita == 2:
        pass
    elif eleccionita == 3:
        pass
    elif eleccionita == 4:
        pass
    elif eleccionita == 5:
        pass
    elif eleccionita == 6:
        pass


def main():
    prosigamitos = True
    while prosigamitos == True:
        if loginito(usuarito, contrasenyita) == True:
            mainQueryta()
            eleccionita = int(input("Introduce el número de la acción: "))
            queQuiereHacerito(usuarito, contrasenyita, eleccionita, tablitaAfectadita)
            quiereContinuaarito = input("¿Desea continuar? (s/n): ")
            if quiereContinuaarito.lower() == "n":
                prosigamitos = False
        else:
            pass
        
main()
    