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

# CLUSTERITZACIÓ

Utlitzarem uan clusterització, i sigui crearem una IP Mestra per a que la aplicació ataqui a un sol servidor, o ben dit servei i ja el servei s'encarrega de dir el servidor que ataca i si un peta, la aplicació seguira sent utilitzada.

Instal·lació:

![1715188444555](image/node_replication/1715188444555.png)

Verificació i Config:

![1715189555045](image/node_replication/1715189555045.png)

Configuració:

[Docs Exemples](https://www.haproxy.com/documentation/haproxy-configuration-manual/latest/#2.7)

```
global
        daemon
        maxconn 256

    defaults
        mode tcp
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms

    frontend http-in
        bind 10.94.255.132:5432
        default_backend servers

    backend servers
        server server1 10.94.255.130:5432 maxconn 32
        server server2 10.94.255.131:5432 maxconn 32
```

![1715190238116](image/node_replication/1715190238116.png)

