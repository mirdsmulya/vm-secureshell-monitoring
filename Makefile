all: clean test-env setup exec jump 

test-env: SHELL:=/bin/bash
test-env:
	@/bin/echo -e "\e[1;32mTesting Environment...\e[0m"
	@. test.sh


setup:
	@/bin/echo -e "\e[1;32mSetting up environment...\e[0m"
	@vagrant up

	@/bin/echo -e "\e[1;32mSetting up alphaServer dependencies.. this will take several minutes\e[0m"
	@vagrant ssh alphaServer -c 'cd /vagrant ; . setup.sh > setup.log ; touch setupServer.complete' 
	
	@/bin/echo -e "\e[1;32mSetting up alphaClient-1 dependencies.. this will take several minutes\e[0m"	
	@vagrant ssh alphaClient-1 -c 'cd /vagrant ; . setup.sh > setup.log ; touch setupClient-1.complete'
	
	@/bin/echo -e "\e[1;32mSetting up alphaClient-2 dependencies.. this will take several minutes\e[0m"
	@vagrant ssh alphaClient-2 -c 'cd /vagrant ; . setup.sh > setup.log ; touch setupClient-2.complete' 

	@until [ -f setupServer.complete ] && [ -f setupClient-1.complete ] && [ -f setupClient-2.complete ] ; do sleep 60; done 


exec:
	@echo " "
	@/bin/echo -e "\e[1;32m ***** Starting alphaClient-1 and alphaClient-2 application *****\e[0m"
	@vagrant ssh alphaClient-1 -c 'cd /vagrant ; sudo python alphaClient/clientApp.py' &
	@vagrant ssh alphaClient-2 -c 'cd /vagrant ; sudo python alphaClient/clientApp.py' &

jump:
	@echo " "
	@/bin/echo -e "\e[1;32mJumping to alphaServer...\e[0m"
	vagrant ssh alphaServer
	#cd /vagrant ; sudo python alphaServer/serverApp.py

clean:
	@/bin/echo -e "\e[1;32mClearing Environment...\e[0m"
	@rm *.log *.complete *.txt *.json alphaServer/*.json alphaClient/*.json &
