# Dev Ops New Probelm Quest - AlphaServer and AlphaClient

My solution built in python, and it contains 3 VM (nodes) running on vagrant + virtualbox environment, 2 VM as AlphaClient and 1 VM as AlphaServer.

VM AlphaServer simply will monitor and gather report from AlpaClient. The metric that will be monitor is ssh-login-metric. This monitoring report will be display at AlphaServer console.

For run the configuration environment:
Todo
$ make all


After all vagrant VM is up, 

You can access alphaServer from below command 
$vagrant ssh alphaServer

Then start the service of alphaServer by
$sudo python alphaServer/serverApp.py


You can try to ssh alphaClient VM on another terminal by
$vagrant ssh alphaClient-1
$vagrant ssh alphaClient-2


ps: I run this app on Ubuntu 18.04