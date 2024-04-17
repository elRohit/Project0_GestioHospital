-- Active: 1712759496762@@10.94.255.109@5432@hospitalito@public

CREATE ROLE mediquito;
CREATE ROLE enfermerito;
CREATE ROLE celadorito;
CREATE ROLE recepcionistito;
CREATE ROLE administradorcito_informatiquito;
CREATE ROLE administradorcito_hospitalito;
CREATE ROLE conductorAmbulancito;

GRANT CONNECT ON DATABASE hospitalito TO mediquito;
GRANT CONNECT ON DATABASE hospitalito TO enfermerito;
GRANT CONNECT ON DATABASE hospitalito TO celadorito;
GRANT CONNECT ON DATABASE hospitalito TO recepcionistito;
GRANT CONNECT ON DATABASE hospitalito TO administradorcito_informatiquito;
GRANT CONNECT ON DATABASE hospitalito TO administradorcito_hospitalito;
GRANT CONNECT ON DATABASE hospitalito TO conductorAmbulancito;

GRANT USAGE ON SCHEMA public TO mediquito;
GRANT USAGE ON SCHEMA public TO enfermerito;
GRANT USAGE ON SCHEMA public TO celadorito;
GRANT USAGE ON SCHEMA public TO administradorcito;
GRANT USAGE ON SCHEMA public TO conductorAmbulancito;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE diagnosticos IN SCHEMA public TO mediquito;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE operaciones IN SCHEMA public TO mediquito;
GRANT SELECT ON TABLE quirofanos IN SCHEMA public TO mediquito;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO mediquito;
GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO mediquito;
GRANT SELECT ON TABLE enfermeros_asignados_medico IN SCHEMA public TO mediquito;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes IN SCHEMA public TO mediquito;

GRANT SELECT ON TABLE diagnosticos IN SCHEMA public TO enfermerito;
GRANT SELECT ON TABLE operaciones IN SCHEMA public TO enfermerito;
GRANT SELECT ON TABLE quirofanos IN SCHEMA public TO enfermerito;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO enfermerito;
GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO enfermerito;
GRANT SELECT ON TABLE enfermeros_asignados_medico IN SCHEMA public TO enfermerito;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes IN SCHEMA public TO enfermerito;

GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO celadorito;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO celadorito;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes IN SCHEMA public TO celadorito;

GRANT SELECT ON TABLE pacientes IN SCHEMA public TO recepcionistito;
GRANT SELECT ON TABLE habitaciones IN SCHEMA public TO recepcionistito;
GRANT SELECT ON TABLE reserva_habitacion IN SCHEMA public TO recepcionistito;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administradorcito_informatiquito;

GRANT ALL PRIVILEGES ON TABLE personal IN SCHEMA public TO administradorcito_hospitalito;
