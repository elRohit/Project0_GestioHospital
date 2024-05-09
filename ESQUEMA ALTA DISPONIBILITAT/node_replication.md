# Webgrafia

https://www.servermania.com/kb/articles/setup-postgresql-cluster

# REPLICACIO ENTRE MASTER I SLAVE

MASTER

Configurem els següents paràmetres de configuració al postgres.conf

![1715010623556](image/node_replication/1715010623556.png)

![1715010683222](image/node_replication/1715010683222.png)

![1715010767059](image/node_replication/1715010767059.png)

![1715010902986](image/node_replication/1715010902986.png)

SLAVE

Configurem els següents paràmetres de configuració al postgres.conf

![1715011121946](image/node_replication/1715011121946.png)

![1715027775597](image/node_replication/1715027775597.png)

![1715027823554](image/node_replication/1715027823554.png)

![1715027893015](image/node_replication/1715027893015.png)

MASTER

creem un rol per a fer les repliques
![1715028119002](image/node_replication/1715028119002.png)

Creació d'un slot per a replicacions

![1715028249794](image/node_replication/1715028249794.png)

Ara configurem la autentificacio

![1715028436913](image/node_replication/1715028436913.png)

Finalment reiniciem el servei postgres ambdós servidors:

![1715028693063](image/node_replication/1715028693063.png)

Ara iniciarem la replicacio

Netejem les dades per replicar en el slave:

![1715030264004](image/node_replication/1715030264004.png)

![1715030904492](image/node_replication/1715030904492.png)

MASTER

select * from pg_stat_replication

![1715030973825](image/node_replication/1715030973825.png)

SLAVE

![1715031108118](image/node_replication/1715031108118.png)

#Prova

Creació de base de dades exemple:

![1715031195172](image/node_replication/1715031195172.png)

![1715031233955](image/node_replication/1715031233955.png)

# BALANCEIJ D'APLICACIO

Utilitzarem un script per ablacejar el servidor i que continui funcionant la aplicació des d'on va deixa de funcionar.


```
if ping -c 1 192.168.1.50 &>/dev/null; then
    echo "Ping exitoso"
else
    echo "Ping fallido"
    # Ejecutar el comando para redirigir el contenido
    sudo cat /etc/network/interfaces2 > /etc/network/interfaces
fi
```
Els fitxers, a dins tenen la ip canvaida, i el script , si no va el ping, sobrescriu i reinicia el adaptador de xarxa:

![1715285534400](image/node_replication/1715285534400.png)

Quan el servidor principal no esta actiu, executaem el script per simular:

![1715285753951](image/node_replication/1715285753951.png)

La següent vegada si que funciona ja que pot fer ping a si mateix.