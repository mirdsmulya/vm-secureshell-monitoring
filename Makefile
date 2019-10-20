all: setup exec jump clean

setup:
	@/bin/echo -e "\e[1;32mSetting up environment...\e[0m"
	@vagrant up
	@/bin/echo -e "\e[1;32mSetting up dependencies...\e[0m"
	vagrant ssh alphaServer -c 'cd /vagrant ; . setup.sh > setup.log ; touch setupServer.complete' &
	vagrant ssh alphaClient-1 -c 'cd /vagrant ; . setup.sh > setup.log ; touch setupClient-1.complete' &
	vagrant ssh alphaClient-2 -c 'cd /vagrant ; . setup.sh > setup.log ; touch setupClient-2.complete' & 
	until [ -f setupServer.complete ] && [ -f setupClient-1.complete ] && [ -f setupClient-2.complete ] ; do sleep 60; done 


exec:
	@/bin/echo -e "\e[1;32mExecute the application...\e[0m"
	#vagrant ssh alphaServer -c 'cd /vagrant ; python serverApp.py' &
	vagrant ssh alphaClient-1 -c 'cd /vagrant/alphaClient ; sudo python clientApp.py' &
	vagrant ssh alphaClient-2 -c 'cd /vagrant/alphaClient ; sudo python clientApp.py'

jump:
	@/bin/echo -e "\e[1;32mJumping to alphaServer...\e[0m"
	vagrant ssh alphaServer
	cd /vagrant/alphaServer ; sudo python serverApp.py
clean:
	rm *.log *.complete
