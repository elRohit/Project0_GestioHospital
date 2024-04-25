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
                user=usuarito,
                password=contrasenyita,
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
                user=usuarito,
                password=contrasenyita,
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
                user=usuarito,
                password=contrasenyita,
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
                user=usuarito,
                password=contrasenyita,
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
            print(f"Nombre: {resultadito[0][0]}            ")
            print(f"Apellidos: {resultadito[0][1]}         ")
            print("+----------------------------------------+")
        
        except psycopg2.Error as e:
            
            print("No se ha podido mostrar el médico enlazado, eres enfermera de planta.")
            
    if opcion == 2:
        pacienteID = input("Introce el número de tarjeta sanitaria del paciente: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user=usuarito,
                password=contrasenyita,
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
            
            print("No esta en ninguna habitacion.")
            
    if opcion == 3:
        pacienteID = input("Introce el número de tarjeta sanitaria del paciente: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user=usuarito,
                password=contrasenyita,
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
            
def menuCelador(usuarito, contrasenyita, opcion):
    
    if opcion == 1:
        pacienteID = input("Introce el número de tarjeta sanitaria del paciente: ")
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user=usuarito,
                password=contrasenyita,
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
            
            print("No esta en ninguna habitacion.")

def menuConductorAmbulancia(usuarito, contrasenyita, opcion):
    
    if opcion == 1:
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user=usuarito,
                password=contrasenyita,
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT DISTINCT nombre, apellidos FROM reservas r JOIN pacientes p ON p.id_tarjeta_sanitaria = r.id_tarjeta_sanitaria WHERE r.h_id = 999; "
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|  Pacientes en la habitación de salida  |")
            print("+----------------------------------------+")
            for i in resultadito:
                print(f"| Nombre: {i[0]}  | Apellidos: {i[1]} |")
            print("+----------------------------------------+")
            
            siOno= input("Recogera a estos pacientes en la habitación de salida(s/n)? ")
            
            if siOno == "s":
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"DELETE FROM reservas WHERE h_id = 999;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                connexio.commit()
                cur.close()
                connexio.close()
            else:
                print("Recogida de pacientes cancelada.")
      
        except psycopg2.Error as e:
            
            print("No hay pacientes en la salida.")
            
def menuAdminHospital(usuarito, contrasenyita, opcion):
        
        if opcion == 1:
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT dni, nombre, apellidos FROM personal;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Lista de personal            |")
                print("+----------------------------------------+")
                print("| DNI      | Nombre    | Apellidos       |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} | {i[2]} |")
                
            except psycopg2.Error as e:
                
                print("No se ha podido mostrar la lista de personal.")
                
        if opcion == 2:
            dni = input("Introduce el DNI del trabajador: ")
            nombreTrabajador = input("Introduce el nombre del trabajador: ")
            apellidosTrabajador = input("Introduce el apellido/s del trabajador: ")
            correo = input("Introduce el correo del trabajador: ")
            telefono = input("Introduce el teléfono del trabajador: ")
            direccion = input("Introduce la dirección del trabajador: ")
            try:
                connexio = psycopg2.connect(
                        dbname="hospital",
                        user=usuarito,
                        password=contrasenyita,
                        host="10.94.255.129",
                        port="5432",
                        sslmode="require"
                    )
                SQLita = f"INSERT INTO personal (dni, nombre, apellidos, correo, num_telefono, direccion) VALUES ('{dni}', '{nombreTrabajador}', '{apellidosTrabajador}', '{correo}', '{telefono}', '{direccion}');"
                cur = connexio.cursor()
                cur.execute(SQLita)
                connexio.commit()
                cur.close()
                connexio.close()
                
                print("El trabajador ha sido dado de alta con éxito.")
                
            except psycopg2.Error as e:
                
                print("No se ha podido dar de alta al trabajador o ya esta de alta.")
        
        if opcion == 3:
            dni = input("Introduce el DNI del trabajador: ")
            quiereBorrar = input("¿Está seguro de que quiere borrar este trabajador? (s/n): ")
            if quiereBorrar == "s":
                try:
                    connexio = psycopg2.connect(
                            dbname="hospital",
                            user=usuarito,
                            password=contrasenyita,
                            host="10.94.255.129",
                            port="5432",
                            sslmode="require"
                        )
                    SQLita = f"DELETE FROM personal WHERE dni = '{dni}';"
                    cur = connexio.cursor()
                    cur.execute(SQLita)
                    connexio.commit()
                    cur.close()
                    connexio.close()

                    print("El trabajador ha sido eliminado con éxito.")
                          
                except psycopg2.Error as e:
                        
                        print("No se ha podido eliminar al trabajador.")
            
            else:
                    
                    print("Intento de borrado cancelado.")
                    
def menuRecepcionista(usuarito, contrasenyita, opcion):
        
        if opcion == 1:
            
            try:
                usuarito = input("Introduce el nombre de usuario: ")
                contrasenyita = input("Introduce la contraseña: ")
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"CREATE ROLE {usuarito} LOGIN PASSWORD '{contrasenyita}' IN ROLE paciente;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                connexio.commit()
                cur.close()
                connexio.close()
                
                print("Su usuario ha sido creado con éxito. ")
                
            except psycopg2.Error as e: 
                    
                    print("El usuario no ha podido ser creado.")
                    
        if opcion == 2:
            
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT nombre, apellidos FROM pacientes p JOIN reservas r ON r.id_tarjeta_sanitaria = p.id_tarjeta_sanitaria;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Lista de pacientes           |")
                print("+----------------------------------------+")
                print("| Nombre         | Apellidos             |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                    
                    print("No se ha podido mostrar la lista de pacientes.")
                
                    
            
            
                