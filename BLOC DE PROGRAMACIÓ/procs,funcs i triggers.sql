-- #########################################
-- DNI
-- #########################################
CREATE OR REPLACE FUNCTION public.validar_dni(
    num TEXT
) RETURNS BOOLEAN AS
$$
DECLARE
    dni_upper TEXT;
    dni_regex TEXT;

BEGIN
    -- Convertir a mayúsculas para evitar problemas con las letras
    dni_upper := UPPER(num);

    -- Patrón para DNI
    dni_regex := '^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$';

    -- Patrón para NIE
    --nie_regex := '^[XYZ][0-9]{7}[TRWAGMYFPDXBNJZSQVHLCKE]$';

    -- Comprobar si cumple con el patrón de DNI o NIE
    IF dni_upper ~ dni_regex  THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- #########################################
-- NIE
-- #########################################
CREATE OR REPLACE FUNCTION public.validar_nie(
    num TEXT
) RETURNS BOOLEAN AS
$$
DECLARE
    nie_upper TEXT;
    nie_regex TEXT;

BEGIN
    -- Convertir a mayúsculas para evitar problemas con las letras
    nie_upper := UPPER(num);
    -- Patrón para NIE
    nie_regex := '^[XYZ][0-9]{7}[TRWAGMYFPDXBNJZSQVHLCKE]$';

    -- Comprobar si cumple con el patrón de DNI o NIE
    IF nie_upper ~ nie_regex  THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION validar_tse(numero_tse VARCHAR) RETURNS BOOLEAN AS
$$
DECLARE
    tse_valida BOOLEAN;
    tse_regex TEXT;
BEGIN
    -- Verificar si el número tiene el formato correcto (por ejemplo, 10 dígitos)
    tse_regex := '^[A-Z]{4} [01] \d{6} \d{2} \d$';
    IF numero_tse ~ tse_regex THEN
        tse_valida := TRUE;
    ELSE
        tse_valida := FALSE;
    END IF;

    RETURN tse_valida;
END;
$$ LANGUAGE plpgsql;

SELECT validar_tse('KUKU 0 050202 0 01');


-- #########################################
--Transladar paciente a Habitacion de Salida
-- #########################################
CREATE OR REPLACE PROCEDURE trasladar_pacientes_salida(
	id_paciente VARCHAR(50)
) AS $$
BEGIN 
	UPDATE reservas 
	SET h_id = 999
	WHERE id_tarjeta_sanitaria = id_paciente;
END;
$$ LANGUAGE plpgsql;
--CALL trasladar_pacientes_salida('ADRIANALOPEZ24')
--Validar DNI (Entorn Comprovacions)
--SELECT validar_dni('46279339z');
--Validar NIE (Entorn Comprovacions)
--SELECT validar_nie('46279339z');



















/*
CREATE TABLE audit.pacientes_dados_baja(
	personal varchar(20),
	tse_paciente VARCHAR(50),
	fecha_salida timestamp
)
CREATE OR REPLACE FUNCTION sacar_pacientes()
RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO audit.pacientes_dados_baja(current_user,)
SELECT * FROM reservas;
select user;*/
