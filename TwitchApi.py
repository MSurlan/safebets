import requests


class TwitchAPI():
    def __init__(self):
        self.headers = None

    def auth(self, client_id, client_secret):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'

        try:
            response = requests.post('https://id.twitch.tv/oauth2/token', headers=headers, data=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

        bearer = response.json()['access_token']

        self.headers = {
            'Authorization': f'Bearer {bearer}',
            'Client-Id': client_id,
        }
        print(response.content)
        # fun1.getLogon(client_id=client, bearer_id=bearer)
    # def getLogon(self, client_id,bearer_id):
    #     headers = {
    #         'Content-Type': f'Authorization: Bearer {bearer_id}',
    #         'Client-Id': f'{client_id}'
    #     }
    #     try:
    #         response = requests.get('https://api.twitch.tv/helix/users?login=twitchdev', headers=headers)
    #         response.raise_for_status()
    #     except requests.exceptions.HTTPError as err:
    #         raise SystemExit(err)
    #     except requests.exceptions.RequestException as err:
    #         raise SystemExit(err)
    #     print(response.content)


client = "mv53zjnhyu9172rap77sq95g52dch3"
secret = "ivdz8r3j7edp9dm40gm113j9bgt99n"
# fun1= TwitchAPI()
# fun1.auth(client_id=client, client_secret=secret)
