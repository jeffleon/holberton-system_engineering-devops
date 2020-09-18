#!/usr/bin/python3
""" Create a function that allow a pagination"""
import requests


def recursive(after, sub, hot_list=[]):
    """" Go throw all pages """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(sub, after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json()
        after = results['data']['after']
        for result in results["data"]["children"]:
            hot_list.append(result['data']['title'])
        if after is None:
            return hot_list
        return recursive(after, sub, hot_list)
    else:
        return None


def recurse(subreddit, hot_list=[]):
    """" Aux function"""
    after = ""
    sub = subreddit
    hot_list = recursive(after, sub, hot_list)
    return hot_list
