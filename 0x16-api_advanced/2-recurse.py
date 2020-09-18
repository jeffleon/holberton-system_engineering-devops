#!/usr/bin/python
""" Create a function that allow a pagination"""
from sys import argv
import requests


def recursive(after, sub, hot_list=[]):
    """" Go throw all pages """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(sub, after)
    try:
        response = requests.get(url, headers=headers)
        results = response.json()
        after = results['data']['after']
        for result in results["data"]["children"]:
            hot_list.append(result['data']['title'])
        if after is None:
            return hot_list
        recursive(after, sub, hot_list)
    except(e):
        return None


def recurse(subreddit, hot_list=[]):
    """" Aux function"""
    after = ""
    sub = subreddit
    recursive(after, sub, hot_list)
