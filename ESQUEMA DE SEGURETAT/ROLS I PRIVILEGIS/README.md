# ELS ROLS I ELS SEUS RESPECTIUS PRIVILEGIS

## TAULA DE ROLS

| Rol                     | Permisos                                                                 |
| ----------------------- | ------------------------------------------------------------------------ |
| Medico                  | SELECT, INSERT, UPDATE, DELETE en diagnosticos i operacion. SELECT a quirofanos, habitaciones, reservas, medico_enfermeria i certs camps de pacients |
| Enfermero               | SELECT en diagnosticos, operacion, quirofan, habitaciones, reservas, medico_enfermeria i certs camps de pacients |
| Celador                 | SELECT en reservas, habitaciones y certs camps de pacients |
| Recepcionista           | SELECT en pacientes, habitaciones y reservas |
| Administrador Informatico| Tots els privilegis a totes las taules de l'esquema públic |
| Administrador Hospital  | Tots els privilegis a la taula personal |
| Conductor Ambulancia    | SELECT, INSERT en reservas  |

## DESCRIPCIÓ PER A CADA ROL

- **Medic**: Té permís per seleccionar dades de la taula `medico_enfermeria` i seleccionar els camps `nombre`, `apellidos` i `condiciones_paciente` de la taula `pacientes`.

- **Infermer**: Té permís per seleccionar dades de les taules `diagnosticos`, `operacion`, `quirofano`, `habitacions`, `reservas`, `medico_enfermeria` i seleccionar els camps `nombre`, `apellidos` i `condiciones_paciente` de la taula `pacientes`.

- **Celador**: Té permís per seleccionar dades de les taules `reservas`, `habitaciones` i seleccionar els camps `nombre`, `apellidos` i `condiciones_paciente` de la taula `pacientes`.

- **Recepcionista**: Té permís per seleccionar dades de les taules `pacientes`, `habitaciones` i `reservas`.

- **Administrador Informatico**: Té tots els privilegis a totes les taules a l'esquema públic.

- **Administrador Hospital**: Teniu permís per seleccionar dades de la taula `personal`.

- **Conductor Ambulància**: Té permís per seleccionar i inserir dades a la taula `reservas`.
