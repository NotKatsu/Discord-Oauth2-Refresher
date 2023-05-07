import httpx 

from helpers.file import File

httpx_client: object = httpx.Client()

class Requests:
    def access_token(refresh_token: str, client_id: str, client_secret: str):
            data = {
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }
            
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = httpx.post('https://discord.com/api/v10/oauth2/token', data=data, headers=headers)
            File.add(response.json()['access_token'])