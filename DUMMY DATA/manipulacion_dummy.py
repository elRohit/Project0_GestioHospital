
import csv
import psycopg2
import random
from faker import Faker
import string
import time

# Aqui es guardaran totes les dades del fitxer csv
host_conn = '192.168.1.50'
pswd = 'P@ssw0rd'
faker = Faker('ru_RU')



'''def import_ciutats():
    #Postgres conn
    conn = psycopg2.connect(database="hospital",user="postgres",password="P@ssw0rd",host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    ## Legir el fitxer csv i guardar-lo en un array
    with open('DUMMY DATA/espanya.csv', 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        count = 0
        
        
        print('*'*80)
        cur.execute(f"DELETE FROM audit.ciutats")
        for row in reader:
            filearray_ciutats.append(row)
            count += 1
            
            cur.execute(f"INSERT INTO audit.ciutats VALUES ({row['Codi']},'{row['Nom']}', {row['CodiProvíncia']})")
        print(f'total de registres: {count}')
        cur.close()
        conn.close()

        return filearray_ciutats'''
        

def import_personal(personal):
    
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

    
def metges(metges):
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

def enfermers(qty):
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

def personal_neteja(netejadors):
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

#import_personal(450)
#metges(100)
#enfermers(200)
#personal_neteja(100)
#personal_administracio(50)

def show_loader():
                for i in range(101):
                    print(f"Loading: {i}%")
                    time.sleep(0.1)
                    print("\033[F\033[K", end="")  # Clear the previous line
                print("Loading ==>> Completed!")

def pacients(pacients):

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
        show_loader()
            
        cur.close()
        conn.close()


pacients(100)

'''def visites(visites):
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    for i in range(visites):
        count += 1
        cur.execute(f"INSERT INTO reserves VALUES ({count},'{faker.date_time_this_year()}','{faker.date_time_this_year()}'")
    print(f'total de registres de visites: {count}')
    cur.close()
    conn.close()'''


    


