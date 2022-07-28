from scrapingbee import ScrapingBeeClient
import urllib.parse

def scraping_bee_api(URL):

    client = ScrapingBeeClient(api_key='03BG51NLUPMXKXJ195RQ4P65OZOW2FOYTJ5EQ6PG41DTZ616Y3KY9R039PDGE45IJ6VQGWLJI76GC0XL')

    #endocoded_url = urllib.parse.quote(URL)

    response = client.get(URL,

            params={
                'render_js':'False',
                'wait':'1000',
                'block_ads':'True',
                'country_code':'de',
                'premium_proxy':'True',
                #'json_response':'True',
                'session_id':'156'

            }
    )
    #print(response.content)

    return response.content
