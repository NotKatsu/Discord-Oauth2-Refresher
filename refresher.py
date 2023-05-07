from helpers.requests import Requests

class Refresher:
    def all():
        try:
            with open('refresh_tokens.txt', 'r') as f:
                for line in f.readlines():
                    if line.strip() != '':
                        Requests.access_token(line.strip(), 'client_id', 'client_secret')
        except:
            return False