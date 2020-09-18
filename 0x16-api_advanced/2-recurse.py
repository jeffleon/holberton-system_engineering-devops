#!/usr/bin/python
""" Create a function that allow a pagination"""
import requests
from sys import argv

def recursive(after, sub, hot_list=[]):
    """" Go throw all pages """
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(sub,after)
    try:
        response = requests.get(url, headers=headers)
        results = response.json()
        after = results['data']['after']
        for result in results["data"]["children"]:
            hot_list.append(result['data']['title'])
        if after == None:
            return hot_list
        recursive(after, sub, hot_list)
    except:
        return None
    
def recurse(subreddit, hot_list=[]):
    """" Aux function"""
    after = ""
    sub = subreddit 
    recursive(after, sub, hot_list)

