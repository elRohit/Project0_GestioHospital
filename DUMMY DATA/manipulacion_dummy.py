
import csv
import psycopg2
# Aqui es guardaran totes les dades del fitxer csv
filearray = []
# Psql connection



def import_ciutats():
    #Postgres conn
    conn = psycopg2.connect(database="hospital",user="postgres",password="P@ssw0rd",host="192.168.1.50",port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    ## Legir el fitxer csv i guardar-lo en un array
    with open('DUMMY DATA/espanya.csv', 'r', newline='',encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        count = 0
        
        
        print('*'*80)
        cur.execute(f"DELETE FROM audit.ciutats")
        for row in reader:
            count += 1
            
            cur.execute(f"INSERT INTO audit.ciutats VALUES ({row['Codi']},'{row['Nom']}', {row['CodiProvíncia']})")
        print(f'total de registres: {count}')
        cur.close()
        conn.close()
    # Retornar el array
    return filearray
    
#import_ciutats()

    
    
    


