import requests

API_HEADERS = {
    'Client-ID' : 'oqz05s964t9gomcyuqu6dijgys8dcw',
    'Accept' : 'application/vnd.twitchtv.v5+json',
}


def checkUser(): #returns true if online, false if not
    print("1")
    if 'stream' in requests.Session().get("https://api.twitch.tv/kraken/streams/124422593 ", headers=API_HEADERS).json():
        print("2")
        if requests.Session().get("https://api.twitch.tv/kraken/streams/124422593 ", headers=API_HEADERS).json()['stream'] is not None: #stream is online
            print("3")
        else:
            print("4")
    else:
        print("5")

checkUser()