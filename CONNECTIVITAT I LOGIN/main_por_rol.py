import psycopg2

def menuAdminInformatico(usuarito, contrasenyita, opcion):
    if opcion == 1:
        usuaritoCreado = input("Introduce el nombre de usuario: ")
        contrasenyitaCreada = input("Introduce la contraseña: ")
        print("Ahora debera elegir el rol del usuario. ")
        print("Tiene estas opciones: ")
        print("administrador_informatico, medico, enfermero, celador,")
        print("conductor_ambulancia, administrador_hospital, recepcionista, invitado.")
        rolcitoCrear = input("Introduce su rama profesional (rol): ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            
            SQLita = f"CREATE ROLE {usuaritoCreado} LOGIN PASSWORD '{contrasenyitaCreada}' IN ROLE {rolcitoCrear};"
            
            cur = connexio.cursor()
            cur.execute(SQLita)
            connexio.commit()
            cur.close()
            connexio.close()
            
            print(" Su usuario ha sido creado con éxito. ")  
            
        except psycopg2.Error as e:
            
            print("El usuario no ha podido ser creado.")
    
    if opcion == 2:
        pacienteCreado = input("Introduce el nombre de usuario: ")
        contrasenyitaCreada = input("Introduce la contraseña: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            
            SQLita = f"CREATE ROLE {pacienteCreado} LOGIN PASSWORD '{contrasenyitaCreada}';"
            
            cur = connexio.cursor()
            cur.execute(SQLita)
            connexio.commit()
            cur.close()
            connexio.close()
            
            print("Su paciente ha sido creado con éxito. ")  
            
        except psycopg2.Error as e:
            
            print("El paciente no ha podido ser creado.")
    
    if opcion == 3:
        usuaritoBorrado = input("Introduce el nombre de usuario: ")
        quiereBorrar = input("¿Está seguro de que quiere borrar este usuario? (s/n): ")
        if quiereBorrar == "s":
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                
                SQLita = f"DROP ROLE {usuaritoBorrado};"
                
                cur = connexio.cursor()
                cur.execute(SQLita)
                connexio.commit()
                cur.close()
                connexio.close()
                
                print("Su usuario/paciente ha sido eliminado con exito. ")  
            
            except psycopg2.Error as e:
            
                print("El usuario/paciente no ha podido ser eliminado.")
        
        else:
            
            print("Intento de borrado cancelado.")
            
    if opcion == 4:
        try:
            connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
            
            SQLita = f"SELECT r.rolname AS usuario, r1.rolname AS rol FROM pg_catalog.pg_roles r JOIN pg_catalog.pg_auth_members m ON (m.member = r.oid) JOIN pg_roles r1 ON (m.roleid = r1.oid) WHERE r.rolcanlogin ORDER BY 1;"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Lista de usuarios            |")
            print("+----------------------------------------+")
            print("| Usuario  | Rol                         |")
            print("+----------------------------------------+")
            for i in resultadito:
                print(f"| {i[0]}  | {i[1]}   |")
            print("+----------------------------------------+")
        except psycopg2.Error as e:
            
            print("No se ha podido mostrar la lista de usuarios.")
            
def menuMedico(usuarito, contrasenyita, opcion):
    if opcion == 1:
        paciente = input("Introduce el nombre del paciente: ")
        pacienteApellido = input("Introduce el apellido del paciente: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT condiciones_paciente FROM pacientes WHERE nombre = '{paciente}' AND apellidos = '{pacienteApellido}';"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Historial del paciente       |")
            print("+----------------------------------------+")
            print("El paciente tiene esta condiciones:      |")
            print(resultadito[0][0])
            print("+----------------------------------------+")
            
        except psycopg2.Error as e:
            
            print("No se ha podido mostrar el historial del paciente.")
            
    if opcion == 2:
        pacienteID = input("Introce el número de tarjeta sanitaria del paciente: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT medicamentos FROM diagnosticos WHERE id_tarjeta_sanitaria = '{pacienteID}' ORDER BY id_tarjeta_sanitaria DESC LIMIT 1;"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Medicación del paciente      |")
            print("+----------------------------------------+")
            print("El paciente tiene esta medicación:       |")
            print(resultadito[0][0])
            print("+----------------------------------------+")
            
        except psycopg2.Error as e:
            
            print("No se ha podido mostrar la medicación del paciente.")
            
    if opcion == 3:
        pacienteID = input("Introce el número de tarjeta sanitaria del paciente: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT pl.pl_id, r.h_id FROM reservas r JOIN habitaciones h ON h.h_id = r.h_id JOIN plantas_habitaciones pl ON pl.h_id = h.h_id WHERE id_tarjeta_sanitaria = '{pacienteID}' ORDER BY id_tarjeta_sanitaria DESC LIMIT 1 ;"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Habitación del paciente      |")
            print("+----------------------------------------+")
            print(f"El paciente está en la planta: {resultadito[0][0]}         |")
            print(f"El paciente está en la habitación: {resultadito[0][1]}     |")
            print("+----------------------------------------+")
            
        except psycopg2.Error as e:
            
            print("No se ha podido mostrar la habitación del paciente.")
            
def menuEnfermero(usuarito, contrasenyita, opcion):
    if opcion == 1:
        medicitoDNI = input("Introduce tu DNI: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT pe.nombre, pe.apellidos FROM medico_enfermeria me JOIN enfermeros e ON e.p_id = me.e_id JOIN medicos m ON m.p_id = me.m_id JOIN personal p ON p.p_id = e.p_id JOIN personal pe ON pe.p_id = m.p_id WHERE p.dni = '{medicitoDNI}';" 
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Médico enlazado              |")
            print("+----------------------------------------+")
            print(f"El médico al que está enlazado es:      |")
            print(resultadito[0][0])
            print("+----------------------------------------+")
        
        except psycopg2.Error as e:
            
            print("No se ha podido mostrar el médico enlazado.")
            