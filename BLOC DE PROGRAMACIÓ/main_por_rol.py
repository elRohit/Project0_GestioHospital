import psycopg2

def menuAdminInformatico(usuarito, contrasenyita, opcion):  
    
    if opcion == 1:
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
    
    if opcion == 4:
        try:
            fecha = input("Introduce la fecha de la operación (YYYY-MM-DD): ")
            connexio = psycopg2.connect(
                dbname="hospital",
                user=usuarito,
                password=contrasenyita,
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT pa.nombre, pa.apellidos, p.nombre, p.apellidos, pe.nombre, pe.apellidos, o.q_id, o.fecha_entrada FROM operacion o JOIN pacientes pa ON o.id_tarjeta_sanitaria = pa.id_tarjeta_sanitaria JOIN medicos m ON o.p_id = m.p_id JOIN personal p ON p.p_id = m.p_id JOIN enfermeros en ON en.p_id = o.en_id JOIN personal pe ON pe.p_id = en.p_id WHERE o.fecha_entrada >= '{fecha} 00:00:00.000000';"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Operaciones previstas        |")
            print("+----------------------------------------+")
            contador = 0
            for i in resultadito:
                print(f"El quirofano asignado es: {resultadito[contador][6]}    |")
                print(f"La hora de la operación es: {resultadito[contador][7]} |")
                print("+----------------------------------------+")
                print(f"El paciente que se va a operar es:      |")
                print(f"Nombre: {resultadito[contador][0]}            ")
                print(f"Apellidos: {resultadito[contador][1]}         ")
                print("+----------------------------------------+")
                print(f"El médico que le va a operar es:        |")
                print(f"Nombre: {resultadito[contador][2]}            ")
                print(f"Apellidos: {resultadito[contador][3]}         ")
                print("+----------------------------------------+")
                print(f"La enfermera que asiste es:             |")
                print(f"Nombre: {resultadito[contador][4]}            ")
                print(f"Apellidos: {resultadito[contador][5]}         ")
                print("+--------------------------------------- +")
                print("+--------------------------------------- +")
                contador += 1
            
        except psycopg2.Error as e:
                
                print("No hay operaciones previstas.")
                
    if opcion == 5:
        fecha_entrada = input("Introduce la fecha de la visita (YYYY-MM-DD): ")
        try:
            connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
            SQLita = f"SELECT pa.nombre, pa.apellidos, p.nombre, p.apellidos, d.fecha_entrada FROM diagnosticos d JOIN pacientes pa ON d.id_tarjeta_sanitaria = pa.id_tarjeta_sanitaria JOIN medicos m ON d.p_id = m.p_id JOIN personal p ON p.p_id = m.p_id WHERE fecha_entrada BETWEEN '{fecha_entrada} 00:00:00.000000' AND '{fecha_entrada} 23:59:59.999999';"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Visitas planificadas         |")
            print("+----------------------------------------+")
            contador = 0
            for i in resultadito:
                print(f"El paciente con visita prevista es:     |")
                print(f"Nombre: {resultadito[contador][0]}            ")
                print(f"Apellidos: {resultadito[contador][1]}         ")
                print(f"El médico asignado a la visita:         |")
                print(f"Nombre: {resultadito[contador][2]}            ")
                print(f"Apellidos: {resultadito[contador][3]}         ")
                print(f"La fecha de la visita es:               |")
                print(resultadito[contador][4])
                print("+--------------------------------------- +")
                contador += 1
            
        except psycopg2.Error as e:

            print("No hay visitas planificadas.")
            
    if opcion == 6:
        try:
            connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
            SQLita = f"SELECT q.q_id, am.am_id, qam.cantidad FROM quirofano q JOIN quirofano_aparatos_medicos qam ON qam.q_id = q.q_id JOIN aparatos_medicos am ON am.am_id = qam.am_id WHERE qam.cantidad < am.cantidad;"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|    Aparatos medicos por quirofano      |")
            print("+----------------------------------------+")
            contador = 0
            for i in resultadito:
                print(f"ID del aparato: {resultadito[contador][1]}            ")
                print(f"ID del quirofano: {resultadito[contador][0]}         ")
                print(f"Cantidad: {resultadito[contador][2]}         ")
                print("+--------------------------------------- +")
                contador += 1
            contador = 0
            
        except psycopg2.Error as e:
                
                print("No hay aparatos medicos en los quirofanos.")
    
    if opcion == 7:
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT COUNT(d.id_m), m.nombre_malaltia FROM diagnosticos d JOIN malalties m ON d.id_m = m.id_m GROUP BY m.nombre_malaltia ORDER BY COUNT(d.id_m) DESC;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Enfermedades más comunes     |")
                print("+----------------------------------------+")
                print("| Número de casos | Enfermedad           |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                        
                        print("No se ha podido mostrar las enfermedades más comunes.")
               
def menuEnfermero(usuarito, contrasenyita, opcion):
    
    if opcion == 1:
        try: 
            medicitoDNI = input("Introduce tu DNI: ")
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
            print(f"Nombre: {resultadito[0][0]}            ")
            print(f"Apellidos: {resultadito[0][1]}         ")
            print("+----------------------------------------+")
        
        except:
            
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
            
            
    if opcion == 4:
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT pa.nombre, pa.apellidos, p.nombre, p.apellidos, pe.nombre, pe.apellidos FROM operacion o JOIN pacientes pa ON o.id_tarjeta_sanitaria = pa.id_tarjeta_sanitaria JOIN medicos m ON o.p_id = m.p_id JOIN personal p ON p.p_id = m.p_id JOIN enfermeros en ON en.p_id = o.en_id JOIN personal pe ON pe.p_id = en.p_id;"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|           Operaciones previstas        |")
            print("+----------------------------------------+")
            print(f"El paciente que se va a operar es:      |")
            print(f"Nombre: {resultadito[0][0]}            ")
            print(f"Apellidos: {resultadito[0][1]}         ")
            print(f"El médico que le va a operar es:        |")
            print(f"Nombre: {resultadito[0][2]}            ")
            print(f"Apellidos: {resultadito[0][3]}         ")
            print(f"La enfermeras que asisten son:          |")
            contador = 0
            for i in resultadito:
                print(f"Nombre: {resultadito[contador][4]}            ")
                print(f"Apellidos: {resultadito[contador][5]}    ")    
                contador += 1    
            contador = 0
            print("+--------------------------------------- +")
            
        except psycopg2.Error as e:
                
                print("No hay operaciones previstas.")
                
    if opcion == 5:
        numQuirofano = int(input("Introduce el número de quirofano: "))
        try:
            connexio = psycopg2.connect(
                dbname="hospital",
                user="postgres",
                password="P@ssw0rd",
                host="10.94.255.129",
                port="5432",
                sslmode="require"
            )
            SQLita = f"SELECT am.am_id, am.nombre, qam.cantidad FROM aparatos_medicos am JOIN quirofano_aparatos_medicos qam ON qam.am_id = am.am_id WHERE qam.q_id = {numQuirofano};"
            cur = connexio.cursor()
            cur.execute(SQLita)
            resultadito = cur.fetchall()
            cur.close()
            connexio.close()
            print("+----------------------------------------+")
            print("|    Aparatos medicos por quirofano      |")
            print("+----------------------------------------+")
            contador = 0
            for i in resultadito:
                print(f"ID del aparato: {resultadito[contador][0]}            ")
                print(f"Nombre del aparato: {resultadito[contador][1]}         ")
                print(f"Cantidad: {resultadito[contador][2]}         ")
                print("+--------------------------------------- +")
                contador += 1
            contador = 0
            
        except psycopg2.Error as e:

            print("No hay aparatos medicos en los quirofanos.")
            
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
                diccionarioEnfermeros = {}
                diccionarioMedicos = {}
                diccionarioVarios = {} 
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                cur = connexio.cursor()
                SQLita = f"SELECT p_id FROM personal;"
                cur.execute(SQLita)
                lista_id = cur.fetchall()
                for p_id in lista_id:
                    id_real = p_id[0]  
                    try:
                        cur.execute(f"SELECT p_id FROM medicos WHERE p_id = {id_real};")
                        resultadito2 = cur.fetchall()
                        if resultadito2:
                            cur.execute(f"SELECT dni, nombre, apellidos FROM personal WHERE p_id = {id_real};")
                            resultadito3 = cur.fetchall()
                            diccionarioMedicos[id_real] = resultadito3[0]
                    except psycopg2.Error as e:
                        pass
                    try:
                        cur.execute(f"SELECT p_id FROM enfermeros WHERE p_id = {id_real};")
                        resultadito2 = cur.fetchall()
                        if resultadito2:
                            cur.execute(f"SELECT dni, nombre, apellidos FROM personal WHERE p_id = {id_real};")
                            resultadito3 = cur.fetchall()
                            diccionarioEnfermeros[id_real] = resultadito3[0]
                    except psycopg2.Error as e:
                        pass
                    try:
                        cur.execute(f"SELECT p_id FROM varios WHERE p_id = {id_real};")
                        resultadito2 = cur.fetchall()
                        if resultadito2:
                            cur.execute(f"SELECT p.dni, p.nombre, p.apellidos, v.tipo_de_trabajo FROM personal p JOIN varios v ON p.p_id = v.p_id WHERE v.p_id = {id_real};")
                            resultadito3 = cur.fetchall()
                            diccionarioVarios[id_real] = resultadito3[0]
                    except psycopg2.Error as e:
                        pass
                    id_real = None
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Lista de personal            |")
                print("+----------------------------------------+")
                print("| Enfermeros |")
                print("+----------------------------------------+")
                for i in diccionarioEnfermeros:
                    print(f"| DNI: {diccionarioEnfermeros[i][0]} | Nombre: {diccionarioEnfermeros[i][1]} | Apellidos: {diccionarioEnfermeros[i][2]} |")
                print("+----------------------------------------+")
                print("| Médicos |")
                print("+----------------------------------------+")
                for i in diccionarioMedicos:
                    print(f"| DNI: {diccionarioMedicos[i][0]} | Nombre: {diccionarioMedicos[i][1]} | Apellidos: {diccionarioMedicos[i][2]} |")
                print("+----------------------------------------+")
                print("| Varios |")
                print("+----------------------------------------+")
                for i in diccionarioVarios:
                    print(f"| DNI: {diccionarioVarios[i][0]} | Nombre: {diccionarioVarios[i][1]} | Apellidos: {diccionarioVarios[i][2]} | Tipo de trabajo: {diccionarioVarios[i][3]} |")
                print("+----------------------------------------+")
       
            except psycopg2.Error as e:
                
                print("No se ha podido mostrar la lista de personal.")
                
        if opcion == 2:
            validar_DNI = True
            while validar_DNI:
                dni = input("Introduce el DNI del trabajador: ")
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT public.validar_dni('{dni}');"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                if resultadito[0][0] == True:
                    nombreTrabajador = input("Introduce el nombre del trabajador: ")
                    apellidosTrabajador = input("Introduce el apellido/s del trabajador: ")
                    correo = input("Introduce el correo del trabajador: ")
                    telefono = input("Introduce el teléfono del trabajador: ")
                    direccion = input("Introduce la dirección del trabajador: ")
                    try:
                        connexio = psycopg2.connect(
                                dbname="hospital",
                                user="postgres",
                                password="P@ssw0rd",
                                host="10.94.255.129",
                                port="5432",
                                sslmode="require"
                            )
                        SQLita = f"INSERT INTO personal (dni, nombre, apellidos, correo, num_telefono, direccion) VALUES ('{dni}', '{nombreTrabajador}', '{apellidosTrabajador}', '{correo}', '{telefono}', '{direccion}');"
                        cur = connexio.cursor()
                        cur.execute(SQLita)
                        connexio.commit()
                        print("A que se dedica este trabajador? ")
                        print("Tiene estas opciones: ")
                        print("medico, enfermero, celador, recepcionista, conductor_ambulancia, administrador_hospital, administrador_informatico.")
                        rol = input("Introduce su rama profesional (rol): ")
                        SQLita2 = f"SELECT p_id FROM personal WHERE dni = '{dni}';"
                        cur.execute(SQLita2)
                        resultadito = cur.fetchall()
                        if rol == "medico":
                            SQLita3 = f"INSERT INTO medicos (p_id) VALUES ({resultadito[0][0]});"
                            cur.execute(SQLita3)
                            connexio.commit()
                            
                        if rol == "enfermero":
                            SQLita3 = f"INSERT INTO enfermeros (p_id) VALUES ({resultadito[0][0]});"
                            cur.execute(SQLita3)
                            connexio.commit()

                        if rol == "celador" or rol == "recepcionista" or rol == "conductor_ambulancia" or rol == "administrador_hospital" or rol == "administrador_informatico":
                            SQLita3 = f"INSERT INTO varios (p_id, tipo_de_trabajo) VALUES ({resultadito[0][0]}, '{rol}');"
                            cur.execute(SQLita3)
                            connexio.commit()
                        usuario = nombreTrabajador[0:1] + dni
                        SQLita4 = f"CREATE ROLE {usuario} LOGIN PASSWORD 'P@ssw0rd' IN ROLE {rol};"
                        cur.execute(SQLita4)
                        connexio.commit()
                        cur.close()
                        connexio.close()
                        
                        print("El trabajador ha sido dado de alta con éxito.")
                        print("El trabajador tiene el rol de: " + rol)
                        print(f"Tu usuario es: {usuario}" )
                        print("Tu contraseña es: P@ssw0rd")
                        
                        validar_DNI = False
                        
                    except psycopg2.Error as e:
                        
                        print("No se ha podido dar de alta al trabajador o ya esta de alta.")
                
                if resultadito[0][0] == False:
                    print("El DNI no es válido.")
                    validar_DNI = False
        
        if opcion == 3:
            dni = input("Introduce el DNI del trabajador: ")
            quiereBorrar = input("¿Está seguro de que quiere borrar este trabajador? (s/n): ")
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
                    
        if opcion == 4:
            fechaVisitas = input("Introduce la fecha de la visita (YYYY-MM-DD): ")
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT COUNT(*) FROM diagnosticos WHERE fecha_entrada BETWEEN '{fechaVisitas} 00:00:00.000000' AND '{fechaVisitas} 23:59:59.999999';"
                SQLita2 = f"SELECT pa.nombre, pa.apellidos, p.nombre, p.apellidos, d.fecha_entrada FROM diagnosticos d JOIN pacientes pa ON d.id_tarjeta_sanitaria = pa.id_tarjeta_sanitaria JOIN medicos m ON d.p_id = m.p_id JOIN personal p ON p.p_id = m.p_id WHERE fecha_entrada BETWEEN '{fechaVisitas} 00:00:00.000000' AND '{fechaVisitas} 23:59:59.999999';"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.execute(SQLita2)
                resultadito2 = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|             Visites del dia            |")
                print("+----------------------------------------+")
                for i in resultadito2:
                    print(f"El paciente que ha sido visitado es:     |")
                    print(f"Nombre: {i[0]}            ")
                    print(f"Apellidos: {i[1]}         ")
                    print(f"El médico que le ha visitado es:         |")
                    print(f"Nombre: {i[2]}            ")
                    print(f"Apellidos: {i[3]}         ")
                    print(f"La fecha de la visita es:                |")
                    print(i[4])
                    print("+--------------------------------------- +")
                print(f"El número de visitas del día es: {resultadito[0][0]}")  
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                
                print("No hay o hubo visitas en ese día.")
                
        if opcion == 5:
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT p.dni, p.nombre, p.apellidos, COUNT(*) FROM diagnosticos d JOIN medicos m ON d.p_id = m.p_id JOIN personal p ON p.p_id = m.p_id GROUP BY p.dni, p.nombre, p.apellidos ORDER BY COUNT(*) DESC;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Médicos más activos          |")
                print("+----------------------------------------+")
                print("| DNI      |   Nombre     | Apellidos    | Más visitas atendidas     |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} | {i[2]} | {i[3]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                    
                    print("No se ha podido mostrar los médicos más activos.")
                    
        if opcion == 6:
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT COUNT(d.id_m), m.nombre_malaltia FROM diagnosticos d JOIN malalties m ON d.id_m = m.id_m GROUP BY m.nombre_malaltia ORDER BY COUNT(d.id_m) DESC;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Enfermedades más comunes     |")
                print("+----------------------------------------+")
                print("| Número de casos | Enfermedad           |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                        
                        print("No se ha podido mostrar las enfermedades más comunes.")
                            
def menuRecepcionista(usuarito, contrasenyita, opcion):
        
        if opcion == 1:
            
                id_tarjeta_sanitaria = input("Introduce el número de tarjeta sanitaria del paciente: ")
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT public.validar_tse('{id_tarjeta_sanitaria}');"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close() 
                validar = True
                while validar:
                    if resultadito[0][0] == True:
                        nombre = input("Introduce el nombre del paciente: ")
                        apellidos = input("Introduce los apellidos del paciente: ")
                        fecha_nacimiento = input("Introduce la fecha de nacimiento del paciente (YYYY-MM-DD HH:MM:SS): ")
                        direccion = input("Introduce la dirección del paciente: ")
                        telefono = input("Introduce el teléfono del paciente: ")
                        contacto_emergencia = input("Introduce el contacto de emergencia del paciente: ")
                        condiciones_medicas = input("Introduce las condiciones médicas del paciente: ")
                        try:
                            connexio = psycopg2.connect(
                                dbname="hospital",
                                user="postgres",
                                password="P@ssw0rd",
                                host="10.94.255.129",
                                port="5432",
                                sslmode="require"
                            )
                            SQLita = f"INSERT INTO pacientes (id_tarjeta_sanitaria, nombre, apellidos, fecha_nacimiento, direccion, num_telefono, contacto_emergencia, condiciones_paciente) VALUES ('{id_tarjeta_sanitaria}', '{nombre}', '{apellidos}', '{fecha_nacimiento}.000000', '{direccion}', '{telefono}', '{contacto_emergencia}', '{condiciones_medicas}');"
                            cur = connexio.cursor()
                            cur.execute(SQLita)
                            connexio.commit()
                            usuario = id_tarjeta_sanitaria[0:4] + id_tarjeta_sanitaria[5] + id_tarjeta_sanitaria[7:13] + id_tarjeta_sanitaria[14:16] + id_tarjeta_sanitaria[17]
                            SQLita2 = f"CREATE ROLE {usuario} LOGIN PASSWORD 'P@ssw0rd' IN ROLE paciente;"
                            cur.execute(SQLita2)
                            connexio.commit()
                            cur.close()
                            connexio.close()
                            print("El paciente ha sido dado de alta con éxito.")
                            print(f"Tu usuario es: {usuario}")
                            print("Tu contraseña es: P@ssw0rd")
                            
                            validar = False
                        
                        except psycopg2.Error as e: 
                            
                            print("El usuario no ha podido ser creado.")
                            validar = False
                            
                    if resultadito[0][0] == False:
                        print("El número de tarjeta sanitaria no es válido.")
                        validar = False
                    
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
                         
        if opcion == 3:
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT h.h_id, ph.pl_id FROM habitaciones h LEFT JOIN reservas r ON h.h_id = r.h_id LEFT JOIN plantas_habitaciones ph ON h.h_id = ph.h_id WHERE r.h_id IS NULL;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Habitaciones libres          |")
                print("+----------------------------------------+")
                print("| Habitación | Planta                    |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                    
                    print("No se hay habitaciones libres.")
    
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
                SQLita = f"SELECT h.h_id, ph.pl_id FROM habitaciones h JOIN reservas r ON h.h_id = r.h_id JOIN plantas_habitaciones ph ON h.h_id = ph.h_id;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Habitaciones ocupadas        |")
                print("+----------------------------------------+")
                print("| Habitación | Planta                    |")
                print("+----------------------------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                    
                    print("No se hay habitaciones ocupadas.")
                    
        if opcion == 5:
            habitacionID = int(input("Introduce el número de habitación: "))
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user=usuarito,
                    password=contrasenyita,
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT r.diaentrada, r.diaprevistosalida, pa.id_tarjeta_sanitaria, pa.nombre, pa.apellidos FROM reservas r JOIN pacientes pa ON r.id_tarjeta_sanitaria = pa.id_tarjeta_sanitaria WHERE r.h_id = {habitacionID} AND diaentrada > current_timestamp;"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Visitas planificadas         |")
                print("+----------------------------------------+--------------------+")
                print("| Fecha entrada | Fecha salida | Tarjeta | Nombre | Apellidos |")
                print("+----------------------------------------+--------------------+")
                for i in resultadito:
                    print(f"| {i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} |")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                    
                    print("No se hay visitas planificadas.")
                    
        if opcion == 6:
            numeroPlanta = int(input("Introduce el número de planta: "))
            try:
                connexio = psycopg2.connect(
                    dbname="hospital",
                    user="postgres",
                    password="P@ssw0rd",
                    host="10.94.255.129",
                    port="5432",
                    sslmode="require"
                )
                SQLita = f"SELECT COUNT(h.h_id) FROM habitaciones h JOIN plantas_habitaciones ph ON h.h_id = ph.h_id WHERE ph.pl_id = {numeroPlanta};"
                SQLita2 = f"SELECT COUNT(q.q_id) FROM quirofano q WHERE pl_id = {numeroPlanta};"
                SQLita3 = f"SELECT COUNT(e.p_id) FROM enfermeros e FULL JOIN medico_enfermeria me ON me.e_id = e.p_id FULL JOIN medicos m ON m.p_id = me.m_id FULL JOIN operacion op ON op.en_id = e.p_id FULL JOIN quirofano q ON q.q_id = op.q_id WHERE me.e_id IS NULL AND q.pl_id = {numeroPlanta};"
                cur = connexio.cursor()
                cur.execute(SQLita)
                resultadito = cur.fetchall()
                cur.execute(SQLita2)
                resultadito2 = cur.fetchall()
                cur.execute(SQLita3)
                resultadito3 = cur.fetchall()
                cur.close()
                connexio.close()
                print("+----------------------------------------+")
                print("|           Estado de la planta          |")
                print("+----------------------------------------+")
                print(f"Las habitaciones que hay en esta planta: {resultadito[0][0]}")
                print(f"El número de quirofanos en la planta es: {resultadito2[0][0]}")
                print(f"El número de enfermeros en la planta es: {resultadito3[0][0]}")
                print("+----------------------------------------+")
                
            except psycopg2.Error as e:
                    
                    print("No se ha podido mostrar el estado de la planta.")
                    
