# Instal·lació i configuració d'una base de dades

## Introducció
Utilitzarem una base de dades anomenada **PostgreSQL**

# Instal·lació
## Instal·lació de Guest Tools

```
sudo su
mkdir /mnt/cdrom
mount /dev/cdrom /mnt/cdrom
apt install gzip2
/mnt/cdrom/VBoxLinuxAddictions.run
reboot
```
# Instal·lació de PostgreSQL

```
sudo nano /etc/apt/sources.list
deb http://ftp.debian.org/debian stable main contrib non-free non-free-firmware
sudo apt-get update
sudo apt-get upgrade
sudo reboot
sudo apt-get install postgresql postgresql-contrib
```
# Configuració de PostgreSQL
```
sudo nano /etc/postgersql/14/main/postgresql.conf
listen_addresses = '*'
Ctrl+O(Guardar) i Ctrl+X(Sortir)

sudo nano /etc/postgersql/14/main/pg_hba.conf
host    all             all             0.0.0.0/0               scram-sha-256
sudo systemctl restart postgresql.service
```
