CREATE OR REPLACE FUNCTION public.validar_dni(
    num TEXT
) RETURNS BOOLEAN AS
$$
DECLARE
    dni_nie_upper TEXT;
    valid_chars TEXT;
    dni_regex TEXT;
    nie_regex TEXT;
BEGIN
    -- Convertir a mayúsculas para evitar problemas con las letras
    dni_nie_upper := UPPER(num);

    -- Patrón para DNI
    dni_regex := '^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$';

    -- Patrón para NIE
    --nie_regex := '^[XYZ][0-9]{7}[TRWAGMYFPDXBNJZSQVHLCKE]$';

    -- Comprobar si cumple con el patrón de DNI o NIE
    IF dni_nie_upper ~ dni_regex  THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;


SELECT validar_dni_nie('46279339zm');

CREATE TABLE medico_enfermeria(
	m_id INTEGER REFERENCES medicos(p_id),
	e_id INTEGER REFERENCES enfermeros(p_id),
	PRIMARY KEY (m_id,e_id)
);











/*
select * from enfermeros;

INSERT INTO enfermeros VALUES (2,'2 Años en medicina');
INSERT INTO medico_enfermeria values (1,2)
*/