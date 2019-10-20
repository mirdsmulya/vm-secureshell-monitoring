# Dev Ops New Probelm Quest - AlphaServer and AlphaClient

My solution built in python2, and it contains 3 VM (nodes) running on vagrant + virtualbox environment, 2 VM as AlphaClient and 1 VM as AlphaServer.

VM AlphaServer simply will monitor and gather report from AlpaClient. The metric that will be monitor is ssh-login-metric. This monitoring report will be display at AlphaServer console.

For run the configuration environment:
Todo
$ make all


After all vagrant VM is up, console will jump automaticly to AlpahServer


Then start the service 
$sudo python alphaServer/serverApp.py


You can try to ssh alphaClient VM via another terminal session
$vagrant ssh alphaClient-1
$vagrant ssh alphaClient-2


note: user/pass for all vagrant VM: vagrant/vagrant
