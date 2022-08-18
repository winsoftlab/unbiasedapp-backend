from config import Config

def getCredentials():
    cred = dict()
    cred['client_id'] = Config.FACEBOOK_APP_ID
    cred['client_secret'] = Config.FACEBOOK_APP_SECRET
    cred['graph_domain'] ='https://graph.facebook.com'
    cred['graph_version'] = 'v14.0'
    cred['endpoint_base'] = cred['graph_domain'] + '/' + cred['graph_version'] + '/'
    #cred['page_id'] = '106520682159644' #will be gotten from the account info
    #cred['instagram_account_id'] ='17841404369285809'
    #cred['ig_username'] = 'ovensdelight_cakes'

    return cred
