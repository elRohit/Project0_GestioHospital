# Codi Python

# Com fer còpies de seguretat?
Per fer els backups a la nostra base de dades haurem de fer un codi python que ens permeti crear un script per fer el script i que també ens permeti automatitzar-lo.
El script que s'haurá de crear dins de la nostra màquina será en el nostre cas, un script que ens permeti fer una còpia de seguretat a nivell lògic, com el següent:

```
#!/bin/bash
# Dades d'accés a POSTGRESQL server
user="postgres"
export pgpassword="P@ssw0rd"
server="192.168.56.104"
database="hospital
"
# Ruta on vam guardar els arxius de backup
BACKUP_PATH="/etc/postgresql/backups/hospital"
current_date=$(date +"%Y-%m-%d")

# Fem la còpia de totes les bases de dades que hi ha a PostgreSQL server
pg_dump -h $server -U $user $database > $BACKUP_PATH/$current_date.sql;

# Comprimim l'arxiu de backup
gzip $BACKUP_PATH/$current_date.sql

```
# Per què hem decidit fer còpies de seguretat a nivell lògic?
Aquest tipus de backup exporta l' estructura de les taules i les dades sense copiar els arxius de dades reals de la base de dades. Per exemple, la comanda pg_dump realitza un backup lògic, perquè exporta les taules i les dades mitjançant les sentències SQL CREATE TABLE i INSERT.

# Com automatizar les còpies de seguretat?
També ens haurem d'assegurar que el nostre codi ens permeti automatizar aquest script mitjançant crontab, si per exemple, volem realitzar una còpia de seguretat de la base de dades cada dia a les 0:00, hauria de
afegir el següent al crontab:

![crontab_img](images/crontab.png)

# Com restaurar una còpia de seguretat?
Per restaurar una còpia de seguretat, haurem de fer un codi python que ens permeti executar la següent comanda a la màquina que conté la nostra base de dades
`psql -d hr -f 2024-04-17.sql`




