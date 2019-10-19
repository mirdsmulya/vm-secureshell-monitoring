
import glob
import json 
import time

class serverApp(object):

    def __init__(self, previoustResult):
        self.previoustResult = previoustResult


    def mergeJsonFile(self):
        result = []
        for obj in glob.glob('*.json'):
            with open(obj, 'r') as infile:
                result.append(json.load(infile))
        return result


    def checkJsonFile(self, mergedJsonResult):
        if mergedJsonResult == self.previoustResult:
            return False

        self.previoustResult = mergedJsonResult 
        return mergedJsonResult


    def displayOnAlphaServer(self, result):
        resultLen = len(result)
        for i in range(0, resultLen):
            resultList = result[i]
            nodeName = resultList['nodeName'].encode("utf-8")
            logInAttempt = resultList['logInAttempt'].encode("utf-8")
            print "> %r node had %r attempts" % (nodeName, logInAttempt)
        print "--------------------------------"


if __name__ == '__main__':

    print "--------------------------------"
    print "Metric for ssh log-in attempts"
    print "--------------------------------"

    previoustResult = 0
    serverAppClass = serverApp(previoustResult)

    while 1 == 1:
        mergedJsonResult = serverAppClass.mergeJsonFile()
        checkResult = serverAppClass.checkJsonFile(mergedJsonResult)
        if checkResult:
            serverAppClass.displayOnAlphaServer(checkResult)
        time.sleep(1)        
