import requests
import json


class InstagramGraphAPI:

    def __init__(self, *args, **params):
        self.params = params



    def makeApiCall(self, url, endpointParams):
            '''
                A function that sends a get request to the facebook graph API with the
                endpoint params.
                url= api url of the get request,
                endpointParams = API endpoint parameters for the target endpoint.
            '''

            data  = requests.get(url, endpointParams)

            response = json.loads(data.content)

            return response



    def get_account_info(self):

        """
        API Endpoint:
            Endpoint for ACCOUNTS info
            https://graph.facebook.com/{graph-version}/me/accounts?access_token={access_token}

        """
        params = self.params

        url = params['endpoint_base'] + 'me/accounts'

        endpointParams = dict()
        endpointParams['access_token'] = params['access_token']

        return self.makeApiCall(url, endpointParams)


    def get_instagram_account_id(self):

        """
            API ENDPOINT FOR GETTING INSTAGRAM INFO

                https://graph.facebook.com/{graph-version}/{page_id}?access_token={your-access-token}&f
                ields=instagram_business_account

            Returns:
            object: data from endpoint

        """

        params = self.params

        endpointParams = dict()

        endpointParams['access_token'] = params['access_token']
        endpointParams['fields'] = 'instagram_business_account'
        url = params['endpoint_base'] + params['page_id']

        return self.makeApiCall(url, endpointParams)



    def get_user_media(self, pagingUrl=''):
        """
        Get User media
        
        API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_to
            ken={access-token}
        

        Returns:
            object: data from the endpoint

        """
        params = self.params

        endpointParams =  dict()

        endpointParams['fields']= 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username'
        endpointParams['access_token'] = params['access_token']

        json_data= []

        if(''== pagingUrl ):
            url = params['endpoint_base'] + params['instagram_account_id'] + '/media'
            response = self.makeApiCall(url, endpointParams)
            json_data.append(response)
        else:
            url = pagingUrl
            response = self.makeApiCall(url, endpointParams)
            json_data.append(response)
            self.get_user_media(response['paging']['next'] )
            
        return json_data



    def getComments(self):

        """GET Comments from media
        API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-media-id}/comments?fields=like_count,replies,username,text'
        Returns
            object: data from the endpoint
        """
        params = self.params
        endpointParams =dict()
        endpointParams['fields'] ='like_count,replies,username,text'
        endpointParams['access_token'] = params['access_token']
        url = params['endpoint_base'] + params['ig_media_id'] + '/' + 'comments'

        return self.makeApiCall(url, endpointParams)

if __name__ =="__main__":
    from .instagramGetCredentials import getCredentials
    credentials = getCredentials()
    InstagramGraphAPI(credentials)

