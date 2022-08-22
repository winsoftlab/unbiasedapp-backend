from facebook_scraper import get_posts_by_search
import browser_cookie3

def scrape_facebook_post(query, page_num):
    cookie = browser_cookie3.load()
    result = []
    for post in get_posts_by_search(query, cookies='from_browser' , extra_info=False, options={'comments':True}, pages=page_num):
        result.append(post)

    return result
