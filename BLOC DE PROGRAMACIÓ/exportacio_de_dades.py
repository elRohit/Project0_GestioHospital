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
    SQLita = f"SELECT p.nombre, p.apellidos, pa.id_tarjeta_sanitaria, pa.nombre, pa.apellidos, d.fecha_entrada, d.fecha_salida, d.tiene_receta, d.medicamentos, m.nombre_malaltia, p.dni FROM diagnosticos d JOIN personal p ON p.p_id = d.p_id JOIN pacientes pa ON pa.id_tarjeta_sanitaria = d.id_tarjeta_sanitaria FULL JOIN malalties m ON m.id_m = d.id_m WHERE fecha_entrada BETWEEN '{fecha_inicio}.000000' AND '{fecha_fin}.999999' ORDER BY fecha_entrada ASC;"
    cur.execute(SQLita)
    resultadito = cur.fetchall()
    cur.close()
    connexio.close()
    return resultadito

def exportacion_xml(fecha_inicio, fecha_fin):
    contador = 0
    datitos = exportacion_datitos(fecha_inicio, fecha_fin)
    xmlns = "xmlns"
    
    root = ET.Element("visitas", attrib={"xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation": "visitesIRA.xsd"})
    
    
    for datito in datitos:
        ET.indent(root, space="\t", level=0)
        
        
        diagnostico = ET.SubElement(root, "visita")
        ET.indent(diagnostico, space="\t", level=1)
        
        numero_diagnostico = ET.SubElement(diagnostico, "numero_diagnostico")
        numero_diagnostico.text = str(contador)
        ET.indent(diagnostico, space="\t", level=1)
        
        dni_medico = ET.SubElement(diagnostico, "dni_medico")
        dni_medico.text = str(datito[10])
        ET.indent(diagnostico, space="\t", level=1)
        
        nombre_medico = ET.SubElement(diagnostico, "nombre_medico")
        nombre_medico.text = str(datito[0])
        ET.indent(diagnostico, space="\t", level=1)
        
        apellidos_medico = ET.SubElement(diagnostico, "apellidos_medico")
        apellidos_medico.text = str(datito[1])
        ET.indent(diagnostico, space="\t", level=1)
        
        tarjeta_sanitaria_paciente = ET.SubElement(diagnostico, "tarjeta_sanitaria_paciente")
        tarjeta_sanitaria_paciente.text = str(datito[2])
        ET.indent(diagnostico, space="\t", level=1)
        
        nombre_paciente = ET.SubElement(diagnostico, "nombre_paciente")
        nombre_paciente.text = str(datito[3])
        ET.indent(diagnostico, space="\t", level=1)
        
        apellidos_paciente = ET.SubElement(diagnostico, "apellidos_paciente")
        apellidos_paciente.text = str(datito[4])
        ET.indent(diagnostico, space="\t", level=1)
        
        fecha_entrada = ET.SubElement(diagnostico, "fecha_entrada")
        fecha_entrada_fecha = str(datito[5])[0:10]
        fecha_entrada_hora = str(datito[5])[11:19]
        fecha_entrada.text = str(fecha_entrada_fecha + "T" + fecha_entrada_hora)
        ET.indent(diagnostico, space="\t", level=1)
        
        fecha_salida = ET.SubElement(diagnostico, "fecha_salida")
        if datito[6] == None:
            fecha_salida.text = "None"
        else:
            fecha_fin_fecha = str(datito[6])[0:10]
            fecha_fin_hora = str(datito[6])[11:19]
            fecha_salida.text = str(fecha_fin_fecha + "T" + fecha_fin_hora)
        ET.indent(diagnostico, space="\t", level=1)
        
        tiene_receta = ET.SubElement(diagnostico, "tiene_receta")
        tiene_receta.text = str(datito[7])
        ET.indent(diagnostico, space="\t", level=1)
        
        medicamentos = ET.SubElement(diagnostico, "medicamentos")
        medicamentos.text = str(datito[8])
        ET.indent(diagnostico, space="\t", level=1)
        
        nombre_enfermedad = ET.SubElement(diagnostico, "nombre_enfermedad")
        nombre_enfermedad.text = str(datito[9])
        ET.indent(diagnostico, space="\t", level=1)
        
        contador += 1
        ET.indent(root, space="\t", level=0)
    tree = ET.ElementTree(root)
    
    tree.write(f"visites.xml", encoding="utf-8", xml_declaration=True)
    

exportacion_xml(fecha_inicio, fecha_fin)