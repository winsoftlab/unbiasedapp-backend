#from config import Config

def getCredentials():
    cred = dict()
    #cred['access_token'] ='EAAIGwAnPTmwBAOjU1GT6A0UlEfDkAElR97TWD2HjEHlL4OxPVaTZChqunG9t31ZCpS5Pv5U4GnOTReIUMQ8ZCmvGUCfZCc3X5WC5ksXk14bZBq4a7IfvxNezR1NGFMdHPnIq233CuktfXKeK7SjVBpoIdZAHBZBMcDhG8t8RzOoXEpHo9p4DEQ28grNZBDSekkRmhTZBEV5cXPgZDZD'
    cred['client_id'] = '570371821489772'
    cred['client_secret'] = 'e25c75a31392cf8d1b10b09114a77a8e'
    cred['graph_domain'] ='https://graph.facebook.com'
    cred['graph_version'] = 'v14.0'
    cred['endpoint_base'] = cred['graph_domain'] + '/' + cred['graph_version'] + '/'
    cred['page_id'] = '106520682159644' #will be gotten from the account info
    #cred['instagram_account_id'] ='17841404369285809'
    #cred['ig_username'] = 'ovensdelight_cakes'

    return cred
