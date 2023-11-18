# curl -X GET 'https://api.twitch.tv/helix/clips?broadcaster_id=1234&first=5' \
# -H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
# -H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'
import re

import requests
import TwitchApi

api = TwitchApi.TwitchAPI()
api.auth(TwitchApi.client, TwitchApi.secret)

class ClipInfo():
    def __init__(self):
        self.broadcast_id = None
        self.thumbnailURL = None
    def getBroadcasterId(self):
        try:
            response = requests.get("https://api.twitch.tv/helix/users?login=Papaplatte",
                                    headers=api.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        #print(response.content)
        self.broadcast_id = response.json()['data'][0]['id']
        #print(self.broadcast_id)
    def getClipInfo(self):

        try:
            response = requests.get(f'https://api.twitch.tv/helix/clips?broadcaster_id={self.broadcast_id}&first=5', headers=api.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        print(response.content)
        self.thumbnailURL = response.json()['data'][0]['thumbnail_url']
        print(self.thumbnailURL)
    def downloadClipFromUrl(self):
        res = self.thumbnailURL.split('preview')[0]
        res = res.rstrip(res[-1])
        res = res + ".mp4"
        r = requests.get(res, stream= True)
        open(f"videos/video{self.broadcast_id}.mp4", "wb").write(r.content)
fun = ClipInfo()
fun.getBroadcasterId()
fun.getClipInfo()
fun.downloadClipFromUrl()
