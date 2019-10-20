#/bin/bash -e


echo "*********** Get update ************"
yes | sudo apt-get update


echo "*********** Instaling python ************"
yes | sudo apt-get install python

echo "*********** Instaling python-pip ************"
yes | sudo apt-get install python-pip


echo "*********** Instaling Export LC_ALL=C ************"
export LC_ALL=C

echo "*********** Instaling Paramiko ************"
yes | sudo pip install paramiko

echo "*********** Setting Up SSH ************"
sudo sed -i -e '/PermitRootLogin / s/ .*/ yes/' /etc/ssh/sshd_config
sudo sed -i -e '/PasswordAuthentication / s/ .*/ yes/' /etc/ssh/sshd_config
sudo service ssh restart