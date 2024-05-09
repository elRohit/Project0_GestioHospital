import xml.etree.ElementTree as ET
import psycopg2
fecha_inicio = input("Introduce la fecha de inicio de la exportación (formato: YYYY-MM-DD HH:MM:SS): ")
fecha_fin = input("Introduce la fecha final de la exportación (formato: YYYY-MM-DD HH:MM:SS): ")

def exportacion_datitos(fecha_inicio, fecha_fin):
    connexio = psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="P@ssw0rd",
        host="10.94.255.129",
        port="5432",
        sslmode="require"
    )
    cur = connexio.cursor()
    SQLita = f"SELECT p.nombre, p.apellidos, pa.id_tarjeta_sanitaria, pa.nombre, pa.apellidos, d.fecha_entrada, d.fecha_salida, d.tiene_receta, d.medicamentos, m.nombre_malaltia FROM diagnosticos d JOIN personal p ON p.p_id = d.p_id JOIN pacientes pa ON pa.id_tarjeta_sanitaria = d.id_tarjeta_sanitaria JOIN malalties m ON m.id_m = d.id_m WHERE fecha_entrada BETWEEN '{fecha_inicio}.000000' AND '{fecha_fin}.999999' ORDER BY fecha_entrada ASC;"
    cur.execute(SQLita)
    resultadito = cur.fetchall()
    cur.close()
    connexio.close()
    return resultadito

def exportacion_xml(fecha_inicio, fecha_fin):
    contador = 0
    datitos = exportacion_datitos(fecha_inicio, fecha_fin)
    
    root = ET.Element(f"visitas")    
    
    for datito in datitos:
        ET.indent(root, space="\t", level=0)
        
        
        diagnostico = ET.SubElement(root, "visita")
        ET.indent(diagnostico, space="\t", level=1)
        
        numero_diagnostico = ET.SubElement(diagnostico, "numero_diagnostico")
        numero_diagnostico.text = str(contador)
        ET.indent(diagnostico, space="\t", level=1)
        
        fecha_diagnostico = ET.SubElement(diagnostico, "nombre_medico")
        fecha_diagnostico.text = str(datito[0])
        ET.indent(diagnostico, space="\t", level=1)
        
        paciente = ET.SubElement(diagnostico, "apellidos_medico")
        paciente.text = str(datito[1])
        ET.indent(diagnostico, space="\t", level=1)
        
        medico = ET.SubElement(diagnostico, "tarjeta_sanitaria_paciente")
        medico.text = str(datito[2])
        ET.indent(diagnostico, space="\t", level=1)
        
        enfermedad = ET.SubElement(diagnostico, "nombre_paciente")
        enfermedad.text = str(datito[3])
        ET.indent(diagnostico, space="\t", level=1)
        
        tratamiento = ET.SubElement(diagnostico, "apellidos_paciente")
        tratamiento.text = str(datito[4])
        ET.indent(diagnostico, space="\t", level=1)
        
        observaciones = ET.SubElement(diagnostico, "fecha_entrada")
        observaciones.text = str(datito[5])
        ET.indent(diagnostico, space="\t", level=1)
        
        observaciones = ET.SubElement(diagnostico, "fecha_salida")
        observaciones.text = str(datito[6])
        ET.indent(diagnostico, space="\t", level=1)
        
        observaciones = ET.SubElement(diagnostico, "tiene_receta")
        observaciones.text = str(datito[7])
        ET.indent(diagnostico, space="\t", level=1)
        
        observaciones = ET.SubElement(diagnostico, "medicamentos")
        observaciones.text = str(datito[8])
        ET.indent(diagnostico, space="\t", level=1)
        
        observaciones = ET.SubElement(diagnostico, "nombre_enfermedad")
        observaciones.text = str(datito[9])
        ET.indent(diagnostico, space="\t", level=1)
        
        contador += 1
        ET.indent(root, space="\t", level=0)
    tree = ET.ElementTree(root)
    
    tree.write(f"visites.xml", encoding="utf-8", xml_declaration=True)
    

exportacion_xml(fecha_inicio, fecha_fin)