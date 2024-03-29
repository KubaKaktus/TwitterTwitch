from rauth import OAuth2Service
import json
class ExampleOAuth2Client:
    def __init__(self, client_id, client_secret):
        self.access_token = None

        self.service = OAuth2Service(
            name="name",
            client_id="id",
            client_secret="secret",
            access_token_url="https://id.twitch.tv/oauth2/authorize",
            authorize_url="https://id.twitch.tv/oauth2/authorize",
            base_url="https://id.twitch.tv/",
            
            
            
        )

        self.get_access_token()

    def get_access_token(self):
        data = {'code': 'bar',
                'grant_type': 'client_credentials',
                'response_type': "token",
                'scope':"channel%3Amanage%3Apolls+channel%3Aread%3Apolls",
                'redirect_uri': 'http://localhost',
                'state':"xyzABC123"}

        session = self.service.get_auth_session(data=data, decoder=json.loads)

        self.access_token = session.access_token

k = ExampleOAuth2Client('id', 'secret')
print(k.get_access_token())
