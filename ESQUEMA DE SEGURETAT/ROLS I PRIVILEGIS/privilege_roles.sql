-- Active: 1712759496762@@10.94.255.109@5432@hospitalito@

CREATE ROLE medico;
CREATE ROLE enfermero;
CREATE ROLE celador;
CREATE ROLE recepcionista;
CREATE ROLE administrador_informatico;
CREATE ROLE administrador_hospital;
CREATE ROLE conductor_ambulancia;

GRANT CONNECT ON DATABASE hospitalito TO medico;
GRANT CONNECT ON DATABASE hospitalito TO enfermero;
GRANT CONNECT ON DATABASE hospitalito TO celador;
GRANT CONNECT ON DATABASE hospitalito TO recepcionista;
GRANT CONNECT ON DATABASE hospitalito TO administrador_informatico;
GRANT CONNECT ON DATABASE hospitalito TO administrador_hospital;
GRANT CONNECT ON DATABASE hospitalito TO conductor_ambulancia;

GRANT USAGE ON SCHEMA  TO medico;
GRANT USAGE ON SCHEMA  TO enfermero;
GRANT USAGE ON SCHEMA  TO celador;
GRANT USAGE ON SCHEMA  TO administradorcito;
GRANT USAGE ON SCHEMA  TO conductor_ambulancia;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE diagnosticos  TO medico;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE operaciones  TO medico;
GRANT SELECT ON TABLE quirofanos  TO medico;
GRANT SELECT ON TABLE habitaciones  TO medico;
GRANT SELECT ON TABLE reserva_habitacion  TO medico;
GRANT SELECT ON TABLE enfermeros_asignados_medico  TO medico;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes  TO medico;

GRANT SELECT ON TABLE diagnosticos  TO enfermero;
GRANT SELECT ON TABLE operaciones  TO enfermero;
GRANT SELECT ON TABLE quirofanos  TO enfermero;
GRANT SELECT ON TABLE habitaciones  TO enfermero;
GRANT SELECT ON TABLE reserva_habitacion   TO enfermero;
GRANT SELECT ON TABLE enfermeros_asignados_medico   TO enfermero;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes   TO enfermero;

GRANT SELECT ON TABLE reserva_habitacion   TO celador;
GRANT SELECT ON TABLE habitaciones   TO celador;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes   TO celador;

GRANT SELECT ON TABLE pacientes   TO recepcionista;
GRANT SELECT ON TABLE habitaciones   TO recepcionista;
GRANT SELECT ON TABLE reserva_habitacion   TO recepcionista;

GRANT ALL PRIVILEGES ON ALL TABLES   TO administrador_informatico;

GRANT ALL PRIVILEGES ON TABLE personal   TO administrador_hospital;
