import requests
from sys import argv

def recursive(after, sub, hot_list=[]):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(sub,after)
    try:
        response = requests.get(url, headers=headers)
        results = response.json()
        after = results['data']['after']
        if after == None:
            return print(len(hot_list))
        for result in results["data"]["children"]:
            hot_list.append(result['data']['title'])
        recursive(after, sub, hot_list)
    except:
        print(None)
    
def recurse(subreddit, hot_list=[]):
    after = ""
    sub = subreddit 
    recursive(after, sub, hot_list)

