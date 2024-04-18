-- Active: 1712759496762@@10.94.255.109@5432@hospitalito@public

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

GRANT USAGE ON SCHEMA public TO medico;
GRANT USAGE ON SCHEMA public TO enfermero;
GRANT USAGE ON SCHEMA public TO celador;
GRANT USAGE ON SCHEMA public TO administradorcito;
GRANT USAGE ON SCHEMA public TO conductor_ambulancia;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE diagnosticos public TO medico;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE operaciones public TO medico;
GRANT SELECT ON TABLE quirofanos public TO medico;
GRANT SELECT ON TABLE habitaciones public TO medico;
GRANT SELECT ON TABLE reserva_habitacion public TO medico;
GRANT SELECT ON TABLE enfermeros_asignados_medico public TO medico;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes public TO medico;

GRANT SELECT ON TABLE diagnosticos public TO enfermero;
GRANT SELECT ON TABLE operaciones public TO enfermero;
GRANT SELECT ON TABLE quirofanos public TO enfermero;
GRANT SELECT ON TABLE habitaciones public TO enfermero;
GRANT SELECT ON TABLE reserva_habitacion  public TO enfermero;
GRANT SELECT ON TABLE enfermeros_asignados_medico  public TO enfermero;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes  public TO enfermero;

GRANT SELECT ON TABLE reserva_habitacion  public TO celador;
GRANT SELECT ON TABLE habitaciones  public TO celador;
GRANT SELECT nombre, apellidos, condiciones_paciente ON TABLE pacientes  public TO celador;

GRANT SELECT ON TABLE pacientes  public TO recepcionista;
GRANT SELECT ON TABLE habitaciones  public TO recepcionista;
GRANT SELECT ON TABLE reserva_habitacion  public TO recepcionista;

GRANT ALL PRIVILEGES ON ALL TABLES  public TO administrador_informatico;

GRANT ALL PRIVILEGES ON TABLE personal  public TO administrador_hospital;
