import os
import json
import time
import paramiko  

class clientApp(object):

    def __init__(self, previoustAttempt):
        self.previoustAttempt = previoustAttempt


    def collectHostname(self):
        os.system('hostname > hostname')
        hostname = open('hostname', 'r')

        for text in hostname:
            return text.rstrip()


    def collectSSHLog(self):
        os.system('sudo cat /var/log/auth.log | grep Accepted > ssh-attempt-log.txt')
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
        jsonFileName = hostname + ".json"
        json_file = open(jsonFileName, 'w+')
        json_file.write(json.dumps(jsonResult))
        json_file = open(jsonFileName, 'r')
        print jsonResult
        return jsonResult


    def sendToAlphaServer(self, hostname):
        #prepare connection using ssh paramiko
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    
        client.connect('10.0.0.10', username='vagrant', password='vagrant')

        jsonFileNameOnDestination = hostname + '.json'
        jsonFileName = hostname + ".json"

        #json file transfer via sftp
        sftp = client.open_sftp()
        sftp.put(jsonFileName,jsonFileNameOnDestination)
        sftp.close()


if __name__ == "__main__":

    previoustAttempt = 0
    clientAppClass = clientApp(previoustAttempt)
    hostname  = clientAppClass.collectHostname()
    while 1 == 1:
        sshAttempt = clientAppClass.collectSSHLog()
        if clientAppClass.checkSshAttempt(sshAttempt):
            clientAppClass.makeJsonFile(hostname, sshAttempt)
            clientAppClass.sendToAlphaServer(hostname)
        time.sleep(1)
    
