--Pacientes Anonimizados

SECURITY LABEL FOR anon ON COLUMN pacientes.id_tarjeta_sanitarial IS 'MASKED WITH FUNCTION anon.partial(num_telefono,2,$$ 1 980502 0 $$)';
UPDATE public.pacientes SET id_tarjeta_sanitaria = anon.partial(id_tarjeta_sanitaria, 2, $$** 1 980502 0 **$$);