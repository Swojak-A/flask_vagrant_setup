# flask_vagrant_setup
This is a proper setup for a blank Flask app working with nginx for debug/test purposes based on Vagrant.

How-to:

1. Clone repo into dir
2. From console run:
"vagrant up"
According to Vagrant file all updates, nginx + ningx settings and python essentials should be loaded automatically.
3. Log into virtual machine using:
"vagrant ssh"
4. Install Pipenv:
"sudo pip3 install pipenv"
WARNING! Use sudo to add pipenv command to PATH.
5. Go into src folder:
"cd /vagrant/app"
6. Set up Pipenv virtual env
"export PIPENV_VENV_IN_PROJECT=1
    export VIRTUALENV_ALWAYS_COPY=1 
    pipenv install -r path/to/requirements.txt"
7. Run virtual env
"pipenv shell"
8. Run app.py
"python app.py"
9. Your server should be running on 
"44.44.44.4:8000"
