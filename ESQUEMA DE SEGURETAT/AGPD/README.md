# Sobre AGPD

- L'Agència Espanyola de Protecció de Dades és l'organisme encarregat de vetllar pel compliment de la normativa de protecció de dades a Espanya. <br>
- L'objectiu principal de l'Agència és garantir el dret fonamental a la protecció de dades, establert en la Constitució Espanyola i en el Reglament General de Protecció de Dades (RGPD) de la Unió Europea. <br>
- A Espanya, totes les empreses i organitzacions que tractin dades personals han d'estar inscrites en el Registre General de Protecció de Dades, gestionat per l'Agència. <br>
- El compliment de la normativa de protecció de dades és obligatori per a totes les entitats, tant públiques com privades. <br>
- L'Agència Espanyola de Protecció de Dades ofereix assessorament i resolució de consultes relacionades amb la protecció de dades, així com la tramitació de denúncies i reclamacions.

# Document necessari per registrar la informació a l’AGPD.
##### Aquest document té com a objectiu descriure les mesures de seguretat implementades per protegir les dades personals dels pacients i el personal de l'hospital, en compliment amb el RGPD i la LOPDGDD. Els següents nivells fan refèrencia als nivells de mesures de seguretat que haurem d'aplicar a les següents dades:

## Nivell bàsic
**Taula pacientes:**
+ nombre
+ apellidos

**Taula personal**
+	nombre
+	apellidos

## Nivell intermig
**Taula pacientes:**
+	fecha_nacimiento
+	direccion
+	num_telefono

**Taula personal:**
+	correo
+ num_telefono
+ direccion

**Taula diagnósticos:**
+	fecha_entrada
+	fecha_salida

**Taula operaciones:**
+	en_id
+	fecha_entrada
+	fecha_salida
+	ha_sido_operado
+	q_id

**Taula reservas:**
+	h_id
+	diaentrada
+	diaprevistosalida

## Nivell alt
**Taula pacientes:**
+	id_tarjeta_sanitaria
+	contacto_emergencia
+	condiciones_paciente

**Taula personal:**
+ p_id
+ DNI

**Taula diagnósticos:**
+	p_id
+	id_tarjeta_sanitaria
+	tiene_receta
+	medicamentos

**Taula operaciones:**
+	Id_tarjeta_sanitaria
+	p_id

**Taula reservas:**
+	id_tarjeta_sanitaria

# Mesures de seguretat:

## Mesures de Nivell Bàsic
**Control d'Accés:**
+ Contrasenyes segures i canvi periòdic de contrasenyes.
+ Assignació de permisos d'accés basats en rols.

**Còpies de Seguretat:**
+ Realització de còpies de seguretat regulars.
+ Emmagatzematge de còpies en ubicacions segures.

**Registre d'Activitat:**
+ Monitorització i registre d'accés i activitats en el sistema.
+ Mesures de Nivell Mitjà (a més de les bàsiques)

**Xifratge:**
+ Xifratge de dades tant en trànsit com en repòs.

## Control d'Accés Avançat:**
+ Autenticació multifactor per accedir als sistemes i dades.

**Auditories:**
+ Realització d'auditories de seguretat periòdiques per detectar i corregir vulnerabilitats.

**Data Masking:**
+ Aplicació de tècniques de data masking per protegir les dades sensibles en entorns de prova o desenvolupament.

## Mesures de Nivell Alt (a més de les bàsiques i mitjanes)
**Seguretat Física:**
+ Controls estrictes d'accés físic a les instal·lacions on s'emmagatzemen les dades.

**Anonimització i Pseudonimització:**
+ Ús de tècniques d'anonimització i pseudonimització per protegir les dades sensibles.

** Avaluacions d'Impacte:**
+ Realització d'avaluacions d'impacte en la protecció de dades (EIPD) periòdiques.

