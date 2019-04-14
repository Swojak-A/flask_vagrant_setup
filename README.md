# flask_vagrant_setup
This is a proper setup for a blank Flask app working with nginx for debug/test purposes based on Vagrant - box: ```"bento/ubuntu-18.04"```.

## How-to:

1. Clone repo into dir

2. From console run:

```
vagrant up
```

According to Vagrant file all updates, nginx + ningx settings and python essentials should be loaded automatically.

3. Log into virtual machine using:

```
vagrant ssh
```

4. Install Pipenv:

```
sudo pip3 install pipenv
```

WARNING! Use sudo to add pipenv command to PATH.

5. Go into src folder:

```
cd /vagrant/src
```

6. Set up Pipenv virtual env

```
export PIPENV_VENV_IN_PROJECT=1
export VIRTUALENV_ALWAYS_COPY=1
pipenv install -r requirements.txt
```
- PIPENV_VENV_IN_PROJECT is self-explainatory
- VIRTUALENV_ALWAYS_COPY prevents this error originated in Vagrant build for Win 10:
```OSError: [Errno 71] Protocol error: '/usr/lib/python3.6/config-3```

7. Run virtual env

```
pipenv shell
```

8. Run app.py

```
python app.py
```

9. Your server should be running on: ```44.44.44.4:8000```


## Debug

- when running ```app.py``` you encounter ```env: python\r: No such file or directory```:

run ```app.py``` in vim by: 

```
sudo vim /vagrant/src/app.py
```

then administer fallowing command ```:set ff=unix``` and save and quit using ```:wq```
