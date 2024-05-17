import psycopg2
import random
from faker import Faker
import string
import time

# Aqui es guardaran totes les dades del fitxer csv
host_conn = '10.94.255.135'
pswd = 'P@ssw0rd'
faker = Faker('ru_RU')

def clean_all():
    try:
        conn = psycopg2.connect(database="hospital",user="postgres",password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("DELETE FROM reservas")
        cur.execute("DELETE FROM operacion")
        cur.execute("DELETE FROM medico_enfermeria")
        cur.execute("DELETE FROM enfermeros")
        cur.execute("DELETE FROM diagnosticos")
        cur.execute("DELETE FROM medicos")
        cur.execute("DELETE FROM varios")
        cur.execute("DELETE FROM pacientes")
        cur.execute("DELETE FROM personal")
        print("Datos eliminados de las tablas correctamente")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error cleaning data: {e}")

def personal(personal):
    try:
        #Postgres conn
        conn = psycopg2.connect(database="hospital",user="postgres",password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        count = 0
        for i in range(personal):
            count += 1
            random.seed()
            #dni
            num_jn = list()
            ll = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            for i in range(8):
                i = random.randint(1, 9)
                num_jn.append(i)
            dni_final = ''.join(map(str, num_jn)) + ll 
            #num_tel
            num_tel = list()
            for i in range(9):
                i = random.randint(1, 9)
                num_tel.append(i)
            num_tel_final = ''.join(map(str, num_tel))
            cur.execute(f"INSERT INTO personal VALUES ({count},'{dni_final}','{faker.first_name()[:20]}','{faker.last_name()[:20]}','{faker.email()[:50]}',{num_tel_final[:20]},'{faker.address()[:20]}')")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargando ==>> Completado! --> {count} registros insertados en la tabla personal")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting personal data: {e}")

def medicos(metges):
    try:
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        count = 0
        for i in range(metges):
            count += 1
            cur.execute(f"INSERT INTO medicos(p_id,curriculum) VALUES ({i+1},'{faker.job()}')")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargndo ==>> Completado! --> {count} registros insertados en la tabla medicos")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting medicos data: {e}")

def enfermeros(qty):
    try:
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        count = 0
        for i in range(qty):
            count += 1
            p_id = i + 101
            cur.execute(f"INSERT INTO enfermeros(p_id,experiencia) VALUES ({p_id},'{faker.job()}')")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargando ==>> Completado! --> {count} registros insertados en la tabla enfermeros")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting enfermeros data: {e}")

def personal_limpieza(netejadors):
    try:
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        count = 0
        for i in range(netejadors):
            count += 1
            p_id = i + 301
            # Уборка номеров significa neteja 
            cur.execute(f"INSERT INTO varios VALUES ({p_id},'{'Уборка номеров'}')")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargando ==>> Completado! --> {count} registros insertados en la tabla personal_limpieza")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting personal_limpieza data: {e}")

def personal_administracio(administracio):
    try:
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        count = 0
        for i in range(administracio):
            count += 1
            p_id = i + 401
            # администрация significa administració
            cur.execute(f"INSERT INTO varios VALUES ({p_id},'{'администрация'}')")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargando ==>> Completado! --> {count} registros insertados en la tabla personal_administracion")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting personal_administracio data: {e}")

def pacientes(pacients):
    try:
        count = 0
        for _ in range(pacients):
            inicials_nom = faker.first_name()
            inicials_nom_tallat = inicials_nom[:2].upper()
            inicials_cognom = faker.last_name()
            inicials_cognom_tallat = inicials_cognom[:2].upper()
            inicials = inicials_nom_tallat + inicials_cognom_tallat

            sexe_tse = random.choice('01')

            num_tse_naix = ''.join(str(random.randint(1, 9)) for _ in range(6))
            data_naix = faker.date_of_birth()

            id_tses = list()
            for _ in range(3):
                id_tse = random.choice('0123456789')
                id_tses.append(id_tse)
            tse = inicials + ' ' + sexe_tse + ' ' + num_tse_naix + ' ' + id_tse

            num_tel = list()
            for i in range(9):
                i = random.randint(1, 9)
                num_tel.append(i)
            num_tel_final = ''.join(map(str, num_tel))

            conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
            conn.autocommit = True
            cur = conn.cursor()

            count += 1
            cur.execute(f"INSERT INTO pacientes (id_tarjeta_sanitaria, nombre, apellidos, fecha_nacimiento, direccion, num_telefono, contacto_emergencia, condiciones_paciente) VALUES ('{tse}','{inicials_nom}','{inicials_cognom}','{data_naix}','{faker.address()}',{num_tel_final},NULL,True) ON CONFLICT DO NOTHING")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargando ==>> Completado! --> {count} registros insertados en la tabla pacientes")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting pacientes data: {e}")

def visitas(visites):
    try:
        count = 0
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT p_id FROM medicos")
        rows = cur.fetchall()
        pers_ids = list()

        for row in rows:
            pers_ids.append(row[0])

        cur.close()
        cur = conn.cursor()
        pacients_tse = list()
        cur.execute(f"SELECT id_tarjeta_sanitaria FROM pacientes")
        rows2 = cur.fetchall()
        for row1 in rows2:
            pacients_tse.append(row1[0])

        for _ in range(visites):
            count += 1
            data = faker.date_of_birth()
            ts_entrada = faker.date() + ' ' + faker.time()
            ts_sortida = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.mktime(time.strptime(ts_entrada, '%Y-%m-%d %H:%M:%S')) + 1800))
            p_id = random.choice(pers_ids)
            tse = random.choice(pacients_tse)
            medicamentos = ['Paracetamol', 'Ibuprofeno', 'Aspirina', 'Amoxicilina', 'Omeprazol', 'Diazepam', 'Lorazepam', 'Clonazepam', 'Alprazolam', 'Zolpidem', 'Zopiclona', 'Trankimazin', 'Rivotril', 'Lexatin', 'Valium', 'Xanax', 'Orfidal', 'Stilnox', 'Imovane', 'Alplax', 'Dormidina', 'Dormicum']
            cur.execute(f"INSERT INTO diagnosticos (p_id, id_tarjeta_sanitaria,fecha_entrada,fecha_salida,tiene_receta,medicamentos) VALUES ('{p_id}','{tse}','{ts_entrada}','{ts_sortida}','Si','{random.choice(medicamentos)}')")
        print("\033[F\033[K", end="")  # Clear the previous line
        print(f"Cargando ==>> Completado! --> {count} registros insertados en la tabla diagnosticos")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error inserting visitas data: {e}")

def drop_indexos():
    try:
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("DROP INDEX idx_pacientes")
        cur.execute("DROP INDEX idx_diagnosticos")
        cur.execute("DROP INDEX idx_personal")
        cur.execute("DROP INDEX idx_medicos")
        cur.execute("DROP INDEX idx_enfermeros")
        cur.execute("DROP INDEX idx_varios")
        print("Cargando ==>> Completado! --> Índices eliminados")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error dropping indexes: {e}")
def indexos():
    try:
        conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        drop_indexos()
        cur.execute("CREATE INDEX idx_pacientes ON pacientes (id_tarjeta_sanitaria)")
        cur.execute("CREATE INDEX idx_diagnosticos ON diagnosticos (p_id, id_tarjeta_sanitaria)")
        cur.execute("CREATE INDEX idx_personal ON personal (p_id)")
        cur.execute("CREATE INDEX idx_medicos ON medicos (p_id)")
        cur.execute("CREATE INDEX idx_enfermeros ON enfermeros (p_id)")
        cur.execute("CREATE INDEX idx_varios ON varios (p_id)")

        print("\033[F\033[K", end="")  # Clear the previous line
        print("Cargando ==>> Completado! --> Índices creados")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error creating indexes: {e}")

def creacion():
    try:
        clean_all()
        personal(450)
        medicos(100)
        enfermeros(200)
        personal_limpieza(100)
        personal_administracio(50)
        pacientes(50000)
        visitas(100000)
        print("Cargando ==>> Completado! --> Datos insertados en la base de datos")
    except Exception as e:
        print(f"Error in creacion: {e}")
