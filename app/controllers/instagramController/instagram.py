import requests
import json
import datetime
import sys

def get_parameters():

    cred = dict()

    cred['access_token'] = 'EAAFWaj14zrEBAIBG00awP98pFy7Aaa5aeYM26xgdbN2jSduzmZALOELmylmqHtDc87AwIKGknljSyoInKj6kf9iCILoszYdr5YazveqI0i2aMgYkhpWTegcuQNWmMcLqtmnJUXMi0j3KKnzntiHKZB4aF6t8zOsTdp7xU3VwZDZD'
    cred['client_id'] = '376489274560177'
    cred['client_secret'] = 'e25c75a31392cf8d1b10b09114a77a8e'
    cred['graph_domain'] = 'https://graph.facebook.com'
    cred['graph_version'] = 'v14.0'
    cred['endpoint_base'] = cred['graph_domain'] + '/' + cred['graph_version'] + '/'
    cred['page_id'] = '106520682159644'
    cred['instagram_account_id'] ='17841404369285809'
    cred['ig_username'] = 'ovensdelight_cakes'
    

    return cred


def make_api_call(url, endpointParams):
    '''
    A function that sends a get request to the facebook graph API with the
    endpoint params.
    url= api url of the get request,
    endpointParams = API endpoint parameters for the target endpoint.

    '''

    data  = requests.get(url, endpointParams)
    response = json.loads(data.content)

    return response

def debug_token( params ):

    '''
    Returns the allowed permissions for our token
    
    '''

    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']
    # Define URL For checking acess token
    url = params['graph_domain'] + '/debug_token'

    return make_api_call(url, endpointParams)


 #   print("Token Expires: ", datetime.datetime.fromtimestamp(access_token_data['data']['expires_at']))

def debug_long_lived_token( params ):

    '''
    API Endpoint:
    For generating long lived token
        https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
    '''
    url = params['endpoint_base'] + 'oauth/access_token'

    #defining the endpoint parameters
    endpointParams= dict()

    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']
    endpointParams['fb_exchange_token'] = params['access_token']



    return make_api_call(url, endpointParams)

#API Endpoint:
#ENDPOINT FOR ACCESS POST INSIGHT
#https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields} 


def get_account_info(params):

    """
    API Endpoint:
        Endpoint for ACCOUNTS info
        https://graph.facebook.com/{graph-version}/me/accounts?access_token={access_token}

    """

    url = params['endpoint_base'] + 'me/accounts'

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']

    return make_api_call(url, endpointParams)


def get_instagram_account_id(params):

    """
    API ENDPOINT FOR GETTING INSTAGRAM INFO

        https://graph.facebook.com/{graph-version}/{page_id}?access_token={your-access-token}&f
        ields=instagram_business_account

    Returns:
        object: data from endpoint
    """
    endpointParams = dict()

    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'
    url = params['endpoint_base'] + params['page_id']

    return make_api_call(url, endpointParams)


def get_instagram_account_info(params):
    """
    Get info on a users account
    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.usern
        ame({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_cou
        nt,followers_count,media_count,media{caption,like_count,comments_count,media_url,permalink,media_type}}&access_token={access-token}

    Returns:
        object: data from endpoint

    """

    endpointParams= dict()

    endpointParams['fields']='business_discovery.username('+ params['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count,media{caption,like_count,comments_count,media_url,permalink,media_type,media{caption,like_count,comments_count,media_url,permalink,media_type}}}'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base']  + params['instagram_account_id']

    return make_api_call(url, endpointParams)


def get_user_media(params, pagingUrl=''):
    """
    Get User media
    
    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_to
        ken={access-token}
    

    Returns:
        object: data from the endpoint

    """
    endpointParams =  dict()

    endpointParams['fields']= 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username'
    endpointParams['access_token'] = params['access_token']

    json_data= []

    if(''== pagingUrl ):
        url = params['endpoint_base'] + params['instagram_account_id'] + '/media'
        response = make_api_call(url, endpointParams)
        json_data.append(response)
    else:
        url = pagingUrl
        response = make_api_call(url, endpointParams)
        json_data.append(response)
        get_user_media(params, response['paging']['next'] )
        
    return json_data
 
def get_hashtagsInfo(params):

    """
    API ENDPOINT:
        https://graph.facebook.com/{grap-api-version}/ig_hastag_search?user_id={
        user-id}&q={hastag-name}&fields={fields}&access_token={access_token}

    Returns:
        object: data from the endpoint
     
    """

    endpointParams = dict()
    endpointParams['user_id'] = params['instagram_account_id']
    endpointParams['q'] = params['hashtag_name']
    endpointParams['fields'] = 'id,name'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'ig_hashtag_search'

    return make_api_call(url, endpointParams)


def get_hashtagMedia(params):
    """
    Get posts for a hashtag

    API Endpoints:
        https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top-media?u
        ser_id={user-id}&fields={fields}

        https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_medi
        a?user_id={user-id}&fields={fields}
    """
    
    endpointParams = dict()
    endpointParams['user_id'] = params['instagram_account_id']
    endpointParams['fields'] = 'id,children,caption,comment_count,like_count, media_type,media_url,permalink'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] 
    return make_api_call(url, endpointParams)



def getRecentlySearchedHastags(params):
    """Get hashtags a user has recently searched for

    API Endpoints:
        https://graph.facebook.com/{graph-api-verison}/{ig-user-id}/recently_search
        ed_hashtags?fields={fields}

    Returns:
        object: data from the endpoint
    """
    endpointParams= dict()
    endpointParams['fields'] = 'id,name'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id'] + '/' + 'recently_searched_hashtags'

    return make_api_call(url, endpointParams)

def getComments(params):

    """GET Comments from media
    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-media-id}/comments?fields=like_count,replies,username,text'
    Returns
        object: data from the endpoint
    """
    endpointParams =dict()
    endpointParams['fields'] ='like_count,replies,username,text'
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + params['ig_media_id'] + '/' + 'comments'

    return make_api_call(url, endpointParams)




 