
class clientApp(object):

    def __init__:
        self.previoustAttempt = previoustAttempt
        self.commandCLI = commandCLI
    

    def collectHostname(self):
        os.system('cat hostname > hostname')
        hostname = open('hostname', 'r')

        for text in hostname:
            pass
        return text
        

    def collectSSHLog(self):
        os.system(commandCLI)
        logAttempt = open('ssh-attempt-log.txt', 'r')
       
       actualAttempt = 0
        for text in logAttempt:
            actualttempt += 1
       
        return actualAttempt


    def countSshAttempt(self, actualAttempt):
        
        if actualAttempt == self.previoustAttempt:
            return False

        self.previoustAttempt = actualAttempt
        return actualAttempt


    def sendToAlphaServer(self):
        pass


if __name__ == "__main__":
    import os
    previoustAttempt = 0
    commandCLI = "cat /var/log/auth.log | grep Accepted > ssh-attempt-log.txt"

    

