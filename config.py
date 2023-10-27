import spotipy.util as util

username = 'ozdakaac3d5c3izl7tcrrzu7i'
client_id ='49d5708ae93e44cc98d01a16a5f4677b'
client_secret = '8de6296d292e4002bd895bba2f5e8d35'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)