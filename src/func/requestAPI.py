import requests
import json

def getKicks():
    url = "http://13.124.82.89:54401/kickboards"
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return res.status_code
    
def tmpOpenFile():
    file = open("../tmp/kick.json", "r")
    return file.items