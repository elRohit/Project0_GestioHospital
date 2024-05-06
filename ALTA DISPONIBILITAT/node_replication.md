# Webgrafia
https://www.servermania.com/kb/articles/setup-postgresql-cluster

<<<<<<< HEAD
=======
# Comandes

```
sudo apt-update
sudo nano /etc/postgresql/15/main/postgresql.conf
```
![1714139307851](image/node_replication/1714139307851.png)

```
sudo /etc/init.d/postgresql restart
psql
CREATE USER replicator REPLICATION LOGIN CONNECTION LIMIT 3 ENCRYPTED PASSWORD 'P@ssw0rd';
\q
sudo /etc/init.d/postgresql stop
sudo apt install rsync
sudo rsync -av /var/lib/postgresql/15/main/ /var/lib/postgresql/15/main/
```

# PROCESS

`sudo nano /etc/postgresql/15/main/postgresql.conf`

![alt text](../images/bdr/image.png)


>>>>>>> 3338fa389aa067eaa6ffd2ba4597d9d178a744fb


# FINAL VERS

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