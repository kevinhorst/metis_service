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
pip install -r requirements.txt
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
sudo systemctl start microblog
```
to start the service.
The flask server is reachable under http://127.0.0.1:8000/
