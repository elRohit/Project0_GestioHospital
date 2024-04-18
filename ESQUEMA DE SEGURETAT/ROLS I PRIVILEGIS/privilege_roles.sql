-- Active: 1712759496762@@10.94.255.109@5432@hospitalito@public

CREATE ROLE medico;
CREATE ROLE enfermero;
CREATE ROLE celador;
CREATE ROLE recepcionistito;
CREATE ROLE administrador_informatico;
CREATE ROLE administrador_hospital;
CREATE ROLE conductor_ambulancia;

GRANT CONNECT ON DATABASE hospitalito TO medico;
GRANT CONNECT ON DATABASE hospitalito TO enfermero;
GRANT CONNECT ON DATABASE hospitalito TO celador;
GRANT CONNECT ON DATABASE hospitalito TO recepcionistito;
GRANT CONNECT ON DATABASE hospitalito TO administrador_informatico;
GRANT CONNECT ON DATABASE hospitalito TO administrador_hospital;
GRANT CONNECT ON DATABASE hospitalito TO conductor_ambulancia;

GRANT USAGE ON SCHEMA public TO medico;
GRANT USAGE ON SCHEMA public TO enfermero;
GRANT USAGE ON SCHEMA public TO celador;
GRANT USAGE ON SCHEMA public TO administradorcito;
GRANT USAGE ON SCHEMA public TO conductor_ambulancia;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE diagnosticos IN SCHEMA public TO medico;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE operaciones IN SCHEMA public TO medico;
GRANT SELECT ON TABLE quirofanos IN SCHEMA public TO medico;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO medico;
GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO medico;
GRANT SELECT ON TABLE enfermeros_asignados_medico IN SCHEMA public TO medico;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes IN SCHEMA public TO medico;

GRANT SELECT ON TABLE diagnosticos IN SCHEMA public TO enfermero;
GRANT SELECT ON TABLE operaciones IN SCHEMA public TO enfermero;
GRANT SELECT ON TABLE quirofanos IN SCHEMA public TO enfermero;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO enfermero;
GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO enfermero;
GRANT SELECT ON TABLE enfermeros_asignados_medico IN SCHEMA public TO enfermero;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes IN SCHEMA public TO enfermero;

GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO celador;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO celador;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes IN SCHEMA public TO celador;

GRANT SELECT ON TABLE pacientes IN SCHEMA public TO recepcionistito;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO recepcionistito;
GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO recepcionistito;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administrador_informatico;

GRANT ALL PRIVILEGES ON TABLE personal IN SCHEMA public TO administrador_hospital;
