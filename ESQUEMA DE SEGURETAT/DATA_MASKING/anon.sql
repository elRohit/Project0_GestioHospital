-- \c hospital
CREATE EXTENSION anon CASCADE;
SELECT anon.init();
SELECT anon.start_dynamic_masking();
-- SECURITY DEFINER

-- personal (Anonitzar per el metge)
CREATE ROLE metge WITH LOGIN PASSWORD 'P@ssw0rd' IN ROLE medico;

SECURITY LABEL FOR anon ON ROLE metge IS 'MASKED';
SECURITY LABEL FOR anon ON COLUMN public.personal.direccion IS 'MASKED WITH FUNCTION anon.random_address()';
SECURITY LABEL FOR anon ON COLUMN public.personal.num_telefono IS 'MASKED WITH FUNCTION anon.partial(num_telefono, 2,$$*****$$,2)';
SECURITY LABEL FOR anon ON COLUMN public.personal.email IS 'MASKED WITH VALUE "FAKE_EMAIL" ';

--Anonimitzar una taula
SELECT anon.anonymize_table('personal');

<<<<<<< HEAD
=======
SECURITY LABEL FOR anon ON COLUMN pacientes.id_tarjeta_sanitarial IS 'MASKED WITH FUNCTION anon.partial(num_telefono,2,$$ 1 980502 0 $$)';
UPDATE public.pacientes SET id_tarjeta_sanitaria = anon.partial(id_tarjeta_sanitaria, 2, $$** 1 980502 0 **$$);




>>>>>>> 47fbceedca633a923c7cc2ffe28a177f2f2d33e7
