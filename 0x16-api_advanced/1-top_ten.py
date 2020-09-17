import requests
from sys import argv

def top_ten(subreddit):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        results = response.json()
        for result in results["data"]["children"]:
            print(result['data']['title'])
    except:
        print(None)
