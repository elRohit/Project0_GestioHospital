import psycopg2
import csv
import hashlib

def registrar_usuarito():
    nombrecito_usuarito = input("Introduce el nombre del usuario: ")
    contrasenya_usuarito = input("Introduce la contraseña: ")
    print("Pon tu profesión, tienes estas elecciones:")
    print("Doctor/a, medico/a, enfermero/a, celador/a, administrador/a, cond_amb (conductor/a de ambulancia)")
    encriptar_datitos(nombrecito_usuarito, contrasenya_usuarito)
    insertar_usuarito_a_la_bd(nombrecito_usuarito, contrasenya_usuarito)
    
def encriptar_datitos(nombrecito_usuarito, contrasenya_usuarito):
    usuarito_encriptado = hashlib.sha256(nombrecito_usuarito.encode())
    contrasenya_encriptada = hashlib.sha256(contrasenya_usuarito.encode())
    insertar_usuarito_en_csv(usuarito_encriptado, contrasenya_encriptada)
    
def insertar_usuarito_en_csv(usuarito_encriptado, contrasenya_encriptada):
    with open("usuaritos_creados.csv", "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([usuarito_encriptado, contrasenya_encriptada])
        
def insertar_usuarito_a_la_bd(nombrecito_usuarito, contrasenya_usuarito):
    
    profesionita_usuarito = input("Introduce la profesión (tanto en m/f): ")
    
    connexio = psycopg2.connect(
        dbname="hospitalito",
        user="postgres",
        password="P@ssw0rd",
        host="10.94.255.109"
    )
    cur = connexio.cursor()
    
    if profesionita_usuarito.lower() == "doctor" or profesionita_usuarito.lower() == "doctora":
        cur.execute(f"CREATE ROLE {nombrecito_usuarito} LOGIN PASSWORD '{contrasenya_usuarito}' IN ROLE doctorcitos;")
        connexio.commit()
        
    if profesionita_usuarito.lower == "medico" or profesionita_usuarito.lower == "medica":
        cur.execute(f"CREATE ROLE {nombrecito_usuarito} LOGIN PASSWORD '{contrasenya_usuarito}' IN ROLE mediquitos;")
        connexio.commit()
        
    if profesionita_usuarito.lower == "enfermero" or profesionita_usuarito.lower == "enfermera":
        cur.execute(f"CREATE ROLE {nombrecito_usuarito} LOGIN PASSWORD '{contrasenya_usuarito}' IN ROLE enfermeritos;")
        connexio.commit()
        
    if profesionita_usuarito.lower == "celador" or profesionita_usuarito.lower == "celadora":
        cur.execute(f"CREATE ROLE {nombrecito_usuarito} LOGIN PASSWORD '{contrasenya_usuarito}' IN ROLE celadorcitos;")
        connexio.commit()
        
    if profesionita_usuarito.lower == "administrador" or profesionita_usuarito.lower == "administradora":
        cur.execute(f"CREATE ROLE {nombrecito_usuarito} LOGIN PASSWORD '{contrasenya_usuarito}' IN ROLE administradorcitos;")
        connexio.commit()
        
    if profesionita_usuarito.lower == "cond_amb":
        cur.execute(f"CREATE ROLE {nombrecito_usuarito} LOGIN PASSWORD '{contrasenya_usuarito}' IN ROLE cond_ambulancitas;")
        connexio.commit()   

def main_inserir_usuarito():
    registrar_usuarito()