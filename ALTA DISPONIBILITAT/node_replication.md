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

PRIMARY

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

SECONDARY

![alt text](image-4.png)

![alt text](image-6.png)

# FINAL

![alt text](image-7.png)

![alt text](image-8.png)


![alt text](image-9.png)









