CREATE TABLE audit.historial_pacient (
    id INT PRIMARY KEY,
    pacient_id INT,
    visita_date DATE,
    intervencio VARCHAR(255),
    pla_medicacio VARCHAR(255),
    FOREIGN KEY (pacient_id) REFERENCES pacients(id)
);

-- Crear la funció per a insertar un nou historial

CREATE OR REPLACE FUNCTION insert_historial_pacient()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit.historial_pacient (id, pacient_id, visita_date, diagnostic, intervencio, pla_medicacio)
    VALUES (NEW.p_id, NEW.id_tarjeta_sanitaria, NEW.fecha_entrada, NEW.diagnostic, NEW.-, NEW.medicamentos);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear el trigger per a insertar un nou historial
CREATE TRIGGER insert_historial_pacient
AFTER INSERT ON pacientes
FOR EACH ROW
EXECUTE FUNCTION insert_historial_pacient();
