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
    with open ("/Users/dongsikga/development/Makertone/hello-kicktty-ai-server/src/tmp/kick.json", "r") as f:
        data = json.load(f)
    return data['items']