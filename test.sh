#/bin/bash

echo "*********** Get update ************"
yes | sudo apt-get update

echo "*********** Export LC_ALL=C ************"
export LC_ALL=C

echo "*********** Instaling python ************"
yes | sudo apt-get install python

echo "*********** Instaling python-pip ************"
yes | sudo apt-get install python-pip

echo "********** Intalling Pytest ************"
yes | sudo pip install -U pytest

echo "********** Testing Code ************"
pytest -v 
