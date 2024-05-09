
import csv
import psycopg2
import random
from faker import Faker
# Aqui es guardaran totes les dades del fitxer csv
host_conn = '192.168.1.50'
faker = Faker()



def personals():
    conn = psycopg2.connect(database="hospital",user="postgres",password="P@ssw0rd",host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    fucker_data = Faker()
    for fuck in range(150450):
        cur.execute(f"INSERT INTO personal VALUES ({len(fuck)},{fake.first_name()},{fake.last_name()})")
'''filearray_ciutats = []



def import_ciutats():
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

def import_personal():
    #Gen Dades De peersoal
    # Id,dni.nom,cognoms,correu,num_telefon,adreça
    # Dni
    random.seed()
    num_jn = list()
    ll = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(8):
        i = random.randint(1, 9)
        num_jn.append(i)
    print(''.join(map(str, num_jn)) + ll)


    #Nom
    llista_noms = ['Joan','Maria','Pau','Anna','Laura','Pere','Jordi','Marta','Julia','Miquel','Jordina','Jordi','Marc','Carla','Judit','Judith','Alex','Eric','Sara','Pol','Emma','Hector','Aina','Hugo','Ariadna',
                   'Nil','Laia','Jan','Clara','Adrià','Berta','Arnau','Nora','Biel','Alba','Joel','Abril','Èric','Olivia','Èlia','Òscar','Aina','Izan','Lola','Àlex','Jana','Lluc','Ariadna','Pau','Mia','Nil','Ona']
    nom = random.choice(llista_noms)

    #Cognom
    llista_cognoms = ['Garcia','Martinez','Lopez','Gomez','Hernandez','Perez','Gonzalez','Rodriguez','Fernandez','Lopez','Sanchez','Ramirez','Torres','Diaz','Vazquez','Castillo',
                     'Romero','Serrano','Molina','Ortega','Delgado','Suarez','Cortes','Vargas','Rojas','Guerrero','Cruz','Navarro','Vega','Mendez','Rios','Reyes','Jimenez',
                     'Morales','Silva','Ramos','Santos','Blanco','Salazar','Mora','Vargas','Valencia','Paredes','Cabrera','Villa','Peña','Quintero','Duarte','Franco']
    cognom = random.choice(llista_cognoms)
        




    #Postgres conn
    conn = psycopg2.connect(database="hospital",user="postgres",password="P@ssw0rd",host=host_conn,port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    ## Crear un fitxer csv amb dades dummy amb el nom personal.csv i amb modul random
    with open('DUMMY DATA/personal.csv', 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        count = 0
        cur.execute(f"DELETE FROM audit.personal")
        for row in reader:
            count += 1
            cur.execute(f"INSERT INTO public.personal VALUES ({row['Codi']},'{row['Nom']}', '{row['Cognom']}', '{row['CodiCiutat']}')")
        print(f'total de registres: {count}')
        cur.close()
        conn.close()


faker()

    
    
    


