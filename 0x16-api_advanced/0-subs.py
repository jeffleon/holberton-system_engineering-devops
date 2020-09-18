#!/usr/bin/python
""" function to find a subredict """
import requests
from sys import argv

def number_of_subscribers(subreddit):
    """ function to find a subredict """
    url = "https://www.reddit.com/api/search_subreddits.json"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    data = {"query" : subreddit}
    response = requests.post(url, headers=headers, data=data)
    try:
        results = response.json()
        print(results['subreddits'][0]['subscriber_count'])
    except:
        print(0)
