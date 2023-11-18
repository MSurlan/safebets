import requests
import TwitchApi

api = TwitchApi.TwitchAPI()
api.auth(TwitchApi.client, TwitchApi.secret)

def get_top_games():
    url = 'https://api.twitch.tv/helix/games/top'
    response = requests.get(url, params={'first':100}, headers=api.headers)

    games_id = {}
    for game in response.json()['data']:
        games_id[game['name']] = game['id']

    return games_id

games_id = get_top_games()
print(games_id)