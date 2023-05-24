import requests


API_HEADERS = {
    'Client-ID' : 'xxxxx',
    'Accept' : 'application/vnd.twitchtv.v5+json',
}

reqSession = requests.Session()

def checkUser(): #returns true if online, false if not
    url = "https://api.twitch.tv/helix/streams/124422593"

    
    req = reqSession.get(url, headers=API_HEADERS)
    jsondata = req.json()
    if 'stream' in jsondata:
        if jsondata['stream'] is not None: #stream is online
            return True
        else:
            return False
    else: return 0

print(checkUser())
