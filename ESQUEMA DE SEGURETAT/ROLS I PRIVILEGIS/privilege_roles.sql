CREATE ROLE medico;
CREATE ROLE enfermero;
CREATE ROLE celador;
CREATE ROLE recepcionista;
CREATE ROLE administrador_informatico CREATEROLE;
CREATE ROLE administrador_hospital;
CREATE ROLE conductor_ambulancia;
CREATE ROLE paciente;

GRANT CONNECT ON DATABASE hospital TO medico;
GRANT CONNECT ON DATABASE hospital TO enfermero;
GRANT CONNECT ON DATABASE hospital TO celador;
GRANT CONNECT ON DATABASE hospital TO recepcionista;
GRANT CONNECT ON DATABASE hospital TO administrador_informatico;
GRANT CONNECT ON DATABASE hospital TO administrador_hospital;
GRANT CONNECT ON DATABASE hospital TO conductor_ambulancia;
GRANT CONNECT ON DATABASE hospital TO paciente;

GRANT USAGE ON SCHEMA public TO medico;
GRANT USAGE ON SCHEMA public TO enfermero;
GRANT USAGE ON SCHEMA public TO celador;
GRANT USAGE ON SCHEMA public TO recepcionista;
GRANT USAGE ON SCHEMA public TO administrador_informatico;
GRANT USAGE ON SCHEMA public TO administrador_hospital;
GRANT USAGE ON SCHEMA public TO conductor_ambulancia;


GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE diagnosticos TO medico;
GRANT SELECT, INSERT, UPDATE,DELETE ON TABLE operacion TO medico;
GRANT SELECT ON TABLE quirofano TO medico;
GRANT SELECT ON TABLE habitaciones TO medico;
GRANT SELECT ON TABLE reservas TO medico;
GRANT SELECT ON TABLE medico_enfermeria TO medico;
GRANT SELECT ON TABLE pacientes TO medico;
GRANT SELECT ON TABLE enfermeros TO medico;
GRANT SELECT ON TABLE quirofano_aparatos_medicos TO medico;
GRANT SELECT ON TABLE aparatos_medicos TO medico;


GRANT SELECT ON TABLE diagnosticos TO enfermero;
GRANT SELECT ON TABLE operacion TO enfermero;
GRANT SELECT ON TABLE quirofano TO enfermero;
GRANT SELECT ON TABLE habitaciones TO enfermero;
GRANT SELECT ON TABLE reservas TO enfermero;
GRANT SELECT ON TABLE medico_enfermeria TO enfermero;
GRANT SELECT(nombre, apellidos, condiciones_paciente) ON TABLE pacientes TO enfermero;

GRANT SELECT ON TABLE reservas TO celador;
GRANT SELECT ON TABLE habitaciones TO celador;
GRANT SELECT(nombre, apellidos, condiciones_paciente) ON TABLE pacientes TO celador;

GRANT SELECT ON TABLE pacientes TO recepcionista;
GRANT SELECT ON TABLE habitaciones TO recepcionista;
GRANT SELECT ON TABLE reservas TO recepcionista;
GRANT SELECT ON TABLE plantas_habitaciones TO recepcionista;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administrador_informatico;

GRANT SELECT, INSERT ON TABLE personal TO administrador_hospital;
GRANT ALL PRIVILEGIES ON SEQUENCE personal_p_id_seq TO administrador_hospital;
GRANT SELECT ON TABLE diagnosticos TO administrador_hospital;

GRANT SELECT, INSERT ON TABLE reservas TO conductor_ambulancia;
GRANT SELECT (nombre, apellidos) ON TABLE pacientes TO conductor_ambulancia;
