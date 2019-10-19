import pytest
import clientApp
import os

clientAppClass = clientApp.clientApp('0')

def test_hostname():
    result = clientAppClass.collectHostname()
    assert str(result) == "mirdsm-ThinkPad-X220"


def test_collectSSHLog():
    os.system('cat /var/log/auth.log | grep Accepted > ssh-attempt-log.txt')
    logAttempt = open('ssh-attempt-log.txt', 'r')
    actualAttempt = 0
    for text in logAttempt:
        actualttempt += 1

    assert clientAppClass.collectSSHLog() == actualAttempt


def test_checkSshAttempt():
    assert clientAppClass.checkSshAttempt(0) == False
    assert clientAppClass.checkSshAttempt(10) == 10


def test_makeJsonFile():
    hostname = "mirdan"
    loginAttempt = "66"
    expected = {"nodeName":"mirdan", "logInAttempt":"66"}
    assert clientAppClass.makeJsonFile(hostname, loginAttempt) == expected
