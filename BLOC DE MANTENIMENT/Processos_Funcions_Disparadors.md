# Creació de Elements a la Base de Dades de l'hospital

## Creació de Procedures

-  Hem creat una funció per transladar els pacients d'una habitació a una de sortida ja que es donaran de baixa després de estar totalment tractats.

```
CREATE OR REPLACE PROCEDURE trasladar_pacientes_salida(
	id_paciente VARCHAR(50)
) AS $$
BEGIN 
	UPDATE reservas 
	SET h_id = 999
	WHERE id_tarjeta_sanitaria = id_paciente;
END;
$$ LANGUAGE plpgsql;
```
> Execució

```
hospital=# select id_tarjeta_sanitaria from pacientes;
 id_tarjeta_sanitaria
----------------------
 LAGA 1 980502 0 02
 ROFA 1 781012 1 52
(2 rows)

hospital=# insert into reservas values ('LAGA 1 980502 0 02',5,current_timestamp,'2024-05-03 20:00:00.000000');
INSERT 0 1
hospital=# call trasladar_pacientes_salida('LAGA 1 980502 0 02');
CALL
hospital=# select * from reservas;
 id_tarjeta_sanitaria | h_id |         diaentrada         |     diaprevistosalida
----------------------+------+----------------------------+----------------------------
 LAGA 1 980502 0 02   |  999 | 2024-04-25 17:11:53.574604 | 2024-05-03 20:00:00
(1 row)

hospital=#
```

## Creació de funcions
- Crea una funció per validar el dni i nie 

Validació DNI:

```
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
```

Validació NIE:

```
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
```
> Execucio

```
spital=# \df
                                        List of functions
 Schema |            Name            | Result data type |       Argument data types        | Type
--------+----------------------------+------------------+----------------------------------+------
 public | trasladar_pacientes_salida |                  | IN id_paciente character varying | proc
 public | validar_dni                | boolean          | num text                         | func
 public | validar_nie                | boolean          | num text                         | func
 public | validar_tse                | boolean          | numero_tse character varying     | func
(4 rows)


hospital=# select validar_dni('46274335M');
 validar_dni
-------------
 t
(1 row)


hospital=# select validar_dni('4627L4335');
 validar_dni
-------------
 f
(1 row)


hospital=#
```

