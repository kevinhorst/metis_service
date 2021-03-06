# Metis_service
A service calling a flask server. Exposes a REST API, where system information can be queried. Running on Linux, written and runs on Python 3.8.2.
# Installation
install virtual environment with
```
sudo -H pip3 install virtualenv
```
clone the repository 

```
git clone https://github.com/kevinhorst/metis_service.git somedir
```
create the virtual environment
```
cd somedir
virtualenv <name of environment directory>
source <name of environment directory>/bin/activate
```
install libraries
```
pip3 install -r requirements.txt
```
Change WorkingDirectory in metis.service to
your local metis folder

```
WorkingDirectory=/home/*/metis
```

Likewise, change Execstart to reference the right directory.
This is neccessary for now, as they expect an absolute path.

```
ExecStart=/home/*/metis/<name of environment directory>/bin/gunicorn -b localhost:8000 metis:app
```
Move metis.service to 

```
/etc/systemd/system/ 
```
run 

```
sudo systemctl daemon-reload
sudo systemctl start metis
```
to start the service.
The flask server is reachable under http://127.0.0.1:8000/
# Usage
The REST API exposes the following endpoints:

Startpoint:
http://127.0.0.1:8000/index

CPU utilization:

http://127.0.0.1:8000/cpu

RAM utilization:

http://127.0.0.1:8000/ram

Partitions and utilization:

http://127.0.0.1:8000/disk

socket connetions ipv4:

http://127.0.0.1:8000/inet4

socket connetions ipv6:

http://127.0.0.1:8000/inet6

mac address:

http://127.0.0.1:8000/mac
