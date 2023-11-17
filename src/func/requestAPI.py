import requests
import json
from src.func.Kickboard import Kickboard

def getKicks():
    kickboard_info_list = []
    url = "http://3.35.50.22:59295/kickboards"
    res = requests.get(url)
    if res.status_code == 200:
        data = json.loads(res.text)
        for kicks in data['kickboards']:
            kickboard_info_list.append(Kickboard(kicks['id'], kicks['lat'], kicks['lng'], kicks['danger']))
        return kickboard_info_list
    else:
        return []
    
def tmpOpenFile():
    with open ("/Users/dongsikga/development/Makertone/hello-kicktty-ai-server/src/tmp/kick.json", "r") as f:
        data = json.load(f)
    kickboard_info_list = []
    for i in data['items']:
        kickboard_info_list.append(Kickboard(i['id'], i['lat'], i['lng']))
    return kickboard_info_list