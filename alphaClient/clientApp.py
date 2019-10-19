import os
import json
import time

class clientApp(object):

    def __init__(self, previoustAttempt):
        self.previoustAttempt = previoustAttempt


    def collectHostname(self):
        os.system('hostname > hostname')
        hostname = open('hostname', 'r')

        for text in hostname:
            return text.rstrip()


    def collectSSHLog(self):
        os.system('cat /var/log/auth.log | grep Accepted > ssh-attempt-log.txt')
        logAttempt = open('ssh-attempt-log.txt', 'r')
       
        actualAttempt = 0  
        for text in logAttempt:
            actualAttempt += 1
       
        return actualAttempt


    def checkSshAttempt(self, actualAttempt):
        
        if actualAttempt == self.previoustAttempt:
            return False

        self.previoustAttempt = actualAttempt
        return actualAttempt

    def makeJsonFile(self, hostname, attempt ):
        jsonResult = {"nodeName":hostname, "logInAttempt":attempt}
        json_file = open('logFinalInfo.json', 'w+')
        json_file.write(json.dumps(jsonResult))
        json_file = open('logFinalInfo.json', 'r')
        print jsonResult
        return jsonResult


    def sendToAlphaServer(self):
        pass


if __name__ == "__main__":

    previoustAttempt = 0
    clientAppClass = clientApp(previoustAttempt)
    hostname  = clientAppClass.collectHostname()
    while 1 == 1:
        sshAttempt = clientAppClass.collectSSHLog()
        if clientAppClass.checkSshAttempt(sshAttempt):
            clientAppClass.makeJsonFile(hostname, sshAttempt)
            clientAppClass.sendToAlphaServer()
        time.sleep(1)
    
