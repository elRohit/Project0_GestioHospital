-- \c hospital
CREATE EXTENSION anon CASCADE;
SELECT anon.init();
SELECT anon.start_dynamic_masking();
-- SECURITY DEFINER

-- personal (Anonitzar per el metge)
SECURITY LABEL FOR anon ON COLUMN public.personal.direccion IS 'MASKED WITH FUNCTION anon.random_address()';
SECURITY LABEL FOR anon ON COLUMN public.personal.num_telefono IS 'MASKED WITH FUNCTION anon.partial(num_telefono, 2,$$*****$$,2)';
--SECURITY LABEL FOR anon ON COLUMN public.personal.email IS 'MASKED WITH VALUE "FAKE_EMAIL" ';

--Anonimitzar una taula
SELECT anon.anonymize_table('personal');
