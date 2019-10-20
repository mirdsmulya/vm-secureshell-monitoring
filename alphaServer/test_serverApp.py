
import serverApp
import glob
import json
serverAppClass = serverApp.serverApp(0)

def test_mergedJsonFile():
    expected = []
    for obj in glob.glob('*.json'):
        with open(obj, 'r') as infile:
            expected.append(json.load(infile))

    assert serverAppClass.mergeJsonFile() == expected

def test_checkJsonFile():
    expected = [{u'nodeName': u'genjeh', u'logInAttempt': u'666'}]
    mergedJson = [{u'nodeName': u'genjeh', u'logInAttempt': u'666'}]
    assert serverAppClass.checkJsonFile(mergedJson) == expected


def test_displayOnAlphaServer():
    resultInput = [{u'nodeName': u'Genjeh', u'logInAttempt': u'666'}]
    expected = 'Genjeh666'
    assert serverAppClass.displayOnAlphaServer(resultInput) == expected

