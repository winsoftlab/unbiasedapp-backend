from config import Config

def getCredentials():
    cred = dict()
    cred['access_token'] =Config['ACCESS_TOKEN'] or 'EAAFWaj14zrEBAIBG00awP98pFy7Aaa5aeYM26xgdbN2jSduzmZALOELmylmqHtDc87AwIKGknljSyoInKj6kf9iCILoszYdr5YazveqI0i2aMgYkhpWTegcuQNWmMcLqtmnJUXMi0j3KKnzntiHKZB4aF6t8zOsTdp7xU3VwZDZD'
    cred['client_id'] = Config['GRAPH_CLIENT_ID']or '376489274560177'
    cred['client_secret'] = Config['GRAPH_CLIENT_SECRET'] or 'e25c75a31392cf8d1b10b09114a77a8e'
    cred['graph_domain'] =Config['GRAPH_DOMAIN'] or 'https://graph.facebook.com'
    cred['graph_version'] = Config['GRAPH_VERSION'] or 'v14.0'
    cred['endpoint_base'] = cred['graph_domain'] + '/' + cred['graph_version'] + '/'
    cred['page_id'] = '106520682159644' #will be gotten from the account info
    #cred['instagram_account_id'] ='17841404369285809'
    #cred['ig_username'] = 'ovensdelight_cakes'

    return cred