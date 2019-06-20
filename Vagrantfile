# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.network "private_network", ip: "44.44.44.4"

  config.vm.provision "shell", inline: <<-SHELL
    echo "xxxXXXxxx Starting instalation! xxxXXXxxx"

    sudo apt-get update
    
    sudo apt-get -y install nginx
    sudo rm /etc/nginx/sites-enabled/default
    sudo touch /etc/nginx/sites-available/flask_settings
    sudo ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/flask_settings
    sudo echo 'server {
            location / {
                    proxy_pass http://127.0.0.1:8000;
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
            }
    }' >> /etc/nginx/sites-available/flask_settings
    sudo systemctl restart nginx

    sudo apt install -y python3-pip python3-dev build-essential libssl-dev

    sudo pip3 install pipenv

    # cd /vagrant/app
    export PIPENV_VENV_IN_PROJECT=1
    export VIRTUALENV_ALWAYS_COPY=1
    cd /vagrant/app && pipenv install 


    echo "xxxXXXxxx Done installing your virtual machine! xxxXXXxxx"
  SHELL
end

