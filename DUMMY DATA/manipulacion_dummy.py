
import csv
import psycopg2
import random
from faker import Faker
import string
import time

# Aqui es guardaran totes les dades del fitxer csv
host_conn = '192.168.56.10'
pswd = 'P@ssw0rd'
faker = Faker('ru_RU')

def clean_all():
    conn = psycopg2.connect(database="hospital",user="postgres",password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DELETE FROM diagnosticos")
    cur.execute("DELETE FROM enfermeros")
    cur.execute("DELETE FROM medicos")
    cur.execute("DELETE FROM varios")
    cur.execute("DELETE FROM pacientes")
    cur.execute("DELETE FROM personal")
    
    cur.close()
    conn.close()
    
def personal(personal):
    
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
    print(f'total de registres dels personals: {count}')
    cur.close()
    conn.close()

def medicos(metges):
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    
    for i in range(metges):
        count += 1
        cur.execute(f"INSERT INTO medicos(p_id,curriculum) VALUES ({i+1},'{faker.job()}')")
    print(f'total de registres dels metges: {count}')
        
    cur.close()
    conn.close()

def enfermeros(qty):
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    
    for i in range(qty):
        count += 1
        p_id = i + 101
        cur.execute(f"INSERT INTO enfermeros(p_id,experiencia) VALUES ({p_id},'{faker.job()}')")
    print(f'total de registres de enfermers: {count}')
        
    cur.close()
    conn.close()

def personal_limpieza(netejadors):
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    for i in range(netejadors):
        count += 1
        p_id = i + 301
        # Уборка номеров significa neteja 
        cur.execute(f"INSERT INTO varios VALUES ({p_id},'{'Уборка номеров'}')")
    print(f'total de registres de netejadors: {count}')
    cur.close()
    conn.close()

def personal_administracio(administracio):
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    for i in range(administracio):
        count += 1
        p_id = i + 401
        # администрация significa administració
        cur.execute(f"INSERT INTO varios VALUES ({p_id},'{'администрация'}')")
    print(f'total de registres de administarció: {count}')
    cur.close()
    conn.close()

def show_loader():
                for i in range(101):
                    print(f"Loading: {i}%")
                    time.sleep(0.1)
                    print("\033[F\033[K", end="")  # Clear the previous line
                print("Loading ==>> Completed!")

def pacientes(pacients):

    #tse
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

        # Volem crear pacients amb dades dummy, 100.000 pacients i per millorar rendiment crearem indexos.
        
            conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
            conn.autocommit = True
            cur = conn.cursor()
            
            count += 1
            cur.execute(f"INSERT INTO pacientes (id_tarjeta_sanitaria, nombre, apellidos, fecha_nacimiento, direccion, num_telefono, contacto_emergencia, condiciones_paciente) VALUES ('{tse}','{inicials_nom}','{inicials_cognom}','{data_naix}','{faker.address()}',{num_tel_final},NULL,True) ON CONFLICT DO NOTHING")
            print(f'{count} pacient/s creats')
        show_loader()
            
        cur.close()
        conn.close()

def visitas(visites):
    # Consultar id de metges
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
    # Consultar tse de pacients
    cur = conn.cursor()
    pacients_tse = list()
    cur.execute(f"SELECT id_tarjeta_sanitaria FROM pacientes")
    rows2 = cur.fetchall()
    for row1 in rows2:
        pacients_tse.append(row1[0])


    for _ in range(visites):
        count += 1
        # Crear visites
        data = faker.date_of_birth()
        ts_entrada = faker.date() + ' ' + faker.time()
        ts_sortida = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.mktime(time.strptime(ts_entrada, '%Y-%m-%d %H:%M:%S')) + 1800))
        p_id = random.choice(pers_ids)
        tse = random.choice(pacients_tse)
        medicamentos = ['Paracetamol', 'Ibuprofeno', 'Aspirina', 'Amoxicilina', 'Omeprazol', 'Diazepam', 'Lorazepam', 'Clonazepam', 'Alprazolam', 'Zolpidem', 'Zopiclona', 'Trankimazin', 'Rivotril', 'Lexatin', 'Valium', 'Xanax', 'Orfidal', 'Stilnox', 'Imovane', 'Alplax', 'Dormidina', 'Dormicum']
        cur.execute(f"INSERT INTO diagnosticos (p_id, id_tarjeta_sanitaria,fecha_entrada,fecha_salida,tiene_receta,medicamentos) VALUES ('{p_id}','{tse}','{ts_entrada}','{ts_sortida}','Si','{random.choice(medicamentos)}')")
    print(f'total de registres de visites: {count}')
    
    cur.close()
    conn.close()

def indexos():
    psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE INDEX idx_pacientes ON pacientes (id_tarjeta_sanitaria)")
    cur.execute("CREATE INDEX idx_personal ON personal (dni)")
    cur.execute("CREATE INDEX idx_medicos ON medicos (p_id)")
    cur.execute("CREATE INDEX idx_enfermeros ON enfermeros (p_id)")
    cur.execute("CREATE INDEX idx_personal_limpieza ON varios (p_id)")
    cur.execute("CREATE INDEX idx_personal_administracion ON varios (p_id)")
    cur.execute("CREATE INDEX idx_diagnosticos ON diagnosticos (p_id)")
    cur.close()
    conn.close()
    
def creacion():
    # Crear personal
    clean_all()
    personal(450)
    medicos(100)
    enfermeros(200)
    personal_limpieza(100)
    personal_administracio(50)
    pacientes(400)
    visitas(500)
    
    
    
    
# Execs


creacion()


