# Dev Ops New Probelm Quest - AlphaServer and AlphaClient

My solution was built in python2, and it contains 3 VM (nodes) running on vagrant + virtualbox environment, 2 VM as AlphaClient and 1 VM as AlphaServer.

VM AlphaServer simply will monitor and gather report from AlpaClient. The metric that will be monitor is ssh-login-metric. This monitoring report will be display at AlphaServer console.


# Start the App

If your system already has vagrant version 2.0.3 above

Todo
$ make all

If vagrant 2.0.3 or above is not ready yet :

Todo
$make full


After all vagrant VM is up, console will jump automaticaly to AlpahServer


Then start the service by execute below command on alphaServer:
$sudo python alphaServer/serverApp.py


You can try to ssh alphaClient VM via another terminal session to test the system functionality:
$vagrant ssh alphaClient-1
$vagrant ssh alphaClient-2

Then alphaServer will automatically report alphaClient ssh metric on it console.

note: user/pass for all vagrant VM: vagrant/vagrant
