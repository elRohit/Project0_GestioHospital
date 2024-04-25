CREATE TABLE personal (
    p_id SERIAL PRIMARY KEY,
    dni VARCHAR(9) NOT NULL CHECK (LENGTH(dni) = 9),
    nombre VARCHAR(20),
    apellidos VARCHAR(50),
    correo VARCHAR(50) NOT NULL CHECK (correo LIKE '%@%'),
    num_telefono VARCHAR(20) NOT NULL,
    direccion VARCHAR(50)
);

CREATE TABLE especialidad (
    e_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    rama VARCHAR(50) NOT NULL
);

CREATE TABLE pacientes (
    id_tarjeta_sanitaria VARCHAR(20) PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellidos VARCHAR(50),
    fecha_nacimiento TIMESTAMP NOT NULL,
    direccion VARCHAR(50),
    num_telefono VARCHAR(50),
    contacto_emergencia VARCHAR(50),
    condiciones_paciente TEXT NOT NULL
);

CREATE TABLE medicos (
    p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
    e_id INTEGER REFERENCES especialidad(e_id),
    curriculum TEXT
);

CREATE TABLE varios (
    p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
    tipo_de_trabajo VARCHAR(50) NOT NULL
);

CREATE TABLE enfermeros (
    p_id INTEGER REFERENCES personal(p_id) PRIMARY KEY,
    experiencia TEXT
);

CREATE TABLE especialidad_estudios_medicos (
    e_id INTEGER REFERENCES especialidad(e_id) PRIMARY KEY,
    p_id INTEGER REFERENCES medicos(p_id),
    estudios_medicos TEXT,
    zona_estudios_realizados VARCHAR(50)
);

CREATE TABLE medico_enfermeria (
    m_id INTEGER REFERENCES medicos(p_id) PRIMARY KEY,
    e_id INTEGER REFERENCES enfermeros(p_id)
);

CREATE TABLE diagnosticos (
    p_id INTEGER REFERENCES medicos(p_id),
    id_tarjeta_sanitaria VARCHAR(20) REFERENCES pacientes(id_tarjeta_sanitaria),
    fecha_entrada TIMESTAMP NOT NULL,
    fecha_salida TIMESTAMP,
    tiene_receta VARCHAR(2) NOT NULL CHECK (tiene_receta IN ('Si', 'No')),
    medicamentos TEXT CHECK ((tiene_receta = 'Si' AND medicamentos IS NOT NULL) OR tiene_receta = 'No'),
	PRIMARY KEY (p_id, id_tarjeta_sanitaria, fecha_entrada)
);

CREATE TABLE plantas (
    pl_id SERIAL PRIMARY KEY
);

CREATE TABLE habitaciones (
    h_id SERIAL PRIMARY KEY
);

CREATE TABLE plantas_habitaciones (
    h_id SERIAL PRIMARY KEY,
    pl_id INTEGER REFERENCES plantas(pl_id) NOT NULL
);

CREATE TABLE quirofano (
    q_id SERIAL PRIMARY KEY,
    pl_id INTEGER REFERENCES plantas(pl_id) NOT NULL
);

CREATE TABLE aparatos_medicos (
    am_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT NOT NULL,
    cantidad VARCHAR(50) NOT NULL
);

CREATE TABLE quirofano_aparatos_medicos (
    am_id INTEGER REFERENCES aparatos_medicos(am_id) PRIMARY KEY,
    q_id INTEGER REFERENCES quirofano(q_id)
);

CREATE TABLE reservas	(
    id_tarjeta_sanitaria VARCHAR(20) REFERENCES pacientes(id_tarjeta_sanitaria),
    h_id INTEGER REFERENCES habitaciones(h_id),
    diaEntrada TIMESTAMP NOT NULL,
    diaPrevistoSalida TIMESTAMP NOT NULL,
	PRIMARY KEY (id_tarjeta_sanitaria, h_id, diaEntrada)
);

CREATE TABLE operacion (
    id_tarjeta_sanitaria VARCHAR(20) REFERENCES pacientes(id_tarjeta_sanitaria),
    p_id INTEGER REFERENCES medicos(p_id),
    en_id INTEGER REFERENCES enfermeros(en_id),
    fecha_entrada TIMESTAMP NOT NULL,
    fecha_salida TIMESTAMP,
	ha_sido_operado VARCHAR(2) NOT NULL CHECK (ha_sido_operado IN ('Si', 'No')),
	PRIMARY KEY (id_tarjeta_sanitaria, p_id, fecha_entrada)
);
