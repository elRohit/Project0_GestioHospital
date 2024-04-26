# Webgrafia
https://www.servermania.com/kb/articles/setup-postgresql-cluster

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

![1714141394336](image/node_replication/1714141394336.png)

`sudo nano /etc/postgresql/15/main/pg_hba.conf`

![1714141605956](image/node_replication/1714141605956.png)

![1714141764688](image/node_replication/1714141764688.png)

![1714141932942](image/node_replication/1714141932942.png)

![1714142133726](image/node_replication/1714142133726.png)

A l'altre servidor fem lo altre:

![1714142522857](image/node_replication/1714142522857.png)

![1714142903739](image/node_replication/1714142903739.png)




