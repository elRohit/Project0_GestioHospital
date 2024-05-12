
import csv
import psycopg2
import random
from faker import Faker
import string

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
    #cur.close()
    #conn.close()
    ## Crear un fitxer csv amb dades dummy amb el nom personal.csv i amb modul random
    
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
    
def pacients(pacients):

    #tse
    #'XXXX' 0 000000 0 00
    inicial_nombre_2 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    inicial_nombre_2_llista = list()
    for i in range(4):
        _i = inicial_nombre_2 
        inicial_nombre_2_llista.append(_i)
    inicial_nombre_2_final = ''.join(map(str, inicial_nombre_2_llista))
    #XXXX '0' 000000 0 00
    sexe_tse = list()
    sexe_fin = sexe_tse.append(random.choice('01'))
    sexe_final = ''.join(map(str, sexe_fin))
    #XXXX 0 '000000' 0 00
    num_tse_naix = list()
    for i in range(6):
        i = random.randint(1, 9)
        num_tse_naix.append(i)
    num_tse_naix_final = ''.join(map(str, num_tse_naix))
    #XXXX 0 000000 '0 00'
    sexe_tse_naix = list()
    sexe_fin_naix = sexe_tse_naix.append(random.choice('01'))
    

    # Volem crear pacients amb dades dummy, 100.000 pacients i per millorar rendiment crearem indexos.
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    for i in range(pacients):
        count += 1
        cur.execute(f"INSERT INTO pacientes VALUES ({count},'{faker.first_name()[:20]}','{faker.last_name()[:20]}','{faker.email()[:50]}','{faker.address()[:20]}')")
    print(f'total de registres dels pacients: {count}')
    

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


    
    


