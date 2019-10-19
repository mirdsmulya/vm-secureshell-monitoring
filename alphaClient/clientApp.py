import os

class clientApp(object):

    def __init__(self, previoustAttempt, commandCLI):
        self.previoustAttempt = previoustAttempt
        self.commandCLI = commandCLI
    

    def collectHostname(self):
        os.system('hostname > hostname')
        hostname = open('hostname', 'r')

        for text in hostname:
            return text


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


    def sendToAlphaServer(self):
        pass


if __name__ == "__main__":

    previoustAttempt = 0
    clientAppClass = clientApp(previoustAttempt,0)  
    
