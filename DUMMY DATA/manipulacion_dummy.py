
import csv
import psycopg2
import random
from faker import Faker
# Aqui es guardaran totes les dades del fitxer csv
host_conn = '10.94.255.130'
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
        
regs_impr = int(input('Quants registres vols introduir a la taula personal?...'))
def import_personal(regs_impr):
    


    #Postgres conn
    conn = psycopg2.connect(database="hospital",user="postgres",password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    
    count = 0
    for i in range(0,regs_impr):
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
            cur.execute(f"INSERT INTO personal VALUES ({count},'{dni_final}','{faker.first_name()[:20]}','{faker.last_name()[:20]}','{faker.email()[:20]}',{num_tel_final[:20]},'{faker.address()[:20]}')")
    print(f'total de registres: {count}')
    #cur.close()
    #conn.close()
    ## Crear un fitxer csv amb dades dummy amb el nom personal.csv i amb modul random
    
def metges():
    conn = psycopg2.connect(database="hospital",user="postgres", password=pswd,host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    count = 0
    
    for i in range(50):
        count += 1
        o = random.randint(1,101)
        cur.execute(f"INSERT INTO medicos(p_id,curriculum) VALUES ({o},'{faker.job()[:20]}')")
        
#import_personal(regs_impr)
metges()
    

    
    
    


