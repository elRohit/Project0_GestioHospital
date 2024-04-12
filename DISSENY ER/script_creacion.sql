DROP DATABASE IF EXISTS hospitalito;
CREATE DATABASE hospitalito;

CREATE TABLE personal (
	p_id SERIAL PRIMARY KEY,
	dni VARCHAR(9) NOT NULL CHECK (dni LENGTH LIKE 9),
	nombre VARCHAR(20),
	apellidos VARCHAR(50),
	correo VARCHAR(50) NOT NULL CHECK (email LIKE '%@%'),
	num_telefono VARCHAR(20) NOT NULL,
	direccion VARCHAR(50)
)
CREATE TABLE especialidad (
	e_id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	rama VARCHAR(50) NOT NULL
)
CREATE TABLE medicos (
	p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
	e_id INTEGER REFERENCES especialidad(e_id),
	curriculum TEXT
)
CREATE TABLE varios (
	p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
	tipo_de_trabajo VARCHAR(50) NOT NULL
)
CREATE TABLE enfermeros (
	p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
	experiencia TEXT
)
CREATE TABLE especialidad_estudios_medicos (
	e_id INTEGER REFERENCES especialidad(e_id) PRIMARY KEY,
	p_id INTEGER REFERENCES personal(p_id),
	estudios_medicos TEXT,
	zona_estudios_realizados VARCHAR(50)
)
CREATE TABLE medico_enfermeria (
	p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
	cantidad INTEGER NOT NULL

)
CREATE TABLE pacientes (
	id_tarjeta_sanitaria VARCHAR(20) PRIMARY KEY NOT NULL,
	nombre VARCHAR(20) NOT NULL,
	apellidos VARCHAR(50),
	fecha_nacimiento DATE NOT NULL,
	direccion VARCHAR(50),
	num_telefono VARCHAR(50),
	contacto_emergencia VARCHAR(50),
	condiciones_paciente TEXT NOT NULL
)
CREATE TABLE diagnosticos (
	p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
	id_tarjeta_sanitaria INTEGER REFERENCES paciente(id_tarjeta_sanitaria)
	fecha_entrada DATE NOT NULL,
	fecha_salida DATE,
	tiene_receta VARCHAR(2) NOT NULL CHECK (tiene_receta IN ('Si', 'No')),
	medicamentos TEXT (IF tiene_receta = 'Si' THEN medicamentos NOT NULL)
)
CREATE TABLE reservas	(
	id_tarjeta_sanitaria INTEGER REFERENCES paciente(id_tarjeta_sanitaria) PRIMARY KEY,
	p_id INTEGER REFERENCES personal(p_id),
	diaPrevistoEntrada DATE NOT NULL,
	diaPrevistoSalida DATE NOT NULL
)
CREATE TABLE aparatos_medicos (
	am_id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	descripcion TEXT NOT NULL,
	cantidad VARCHAR(50) NOT NULL
)
CREATE TABLE plantas (
	pl_id SERIAL PRIMARY KEY
)
CREATE TABLE habitaciones (
	h_id SERIAL PRIMARY KEY
)
CREATE TABLE plantas_habitaciones (
	h_id SERIAL PRIMARY KEY,
	pl_id INTEGER REFERENCES plantas(pl_id) NOT NULL
)
CREATE TABLE quirofano (
	q_id SERIAL PRIMARY KEY,
	pl_id INTEGER REFERENCES plantas(pl_id) NOT NULL
)

CREATE TABLE quirofano_aparatos_medicos (
	am_id INTEGER REFERENCES aparatos_medicos(am_id) PRIMARY KEY,
	q_id INTEGER REFERENCES quirofano(q_id)
)
CREATE TABLE operacion (
	id_tarjeta_sanitaria INTEGER REFERENCES paciente(id_tarjeta_sanitaria) PRIMARY KEY,
	p_id INTEGER REFERENCES personal(p_id),
	fecha_entrada DATE NOT NULL,
	fecha_salida DATE
)
CREATE TABLE operacion_enfermeria (
	id_tarjeta_sanitaria INTEGER REFERENCES paciente(id_tarjeta_sanitaria) PRIMARY KEY,
	p_id INTEGER REFERENCES personal(p_id),
	cantidad INTEGER NOT NULL
)