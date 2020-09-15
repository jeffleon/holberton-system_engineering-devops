#!/usr/bin/python3
""" Prove API Rest"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Print Tasks """
    Tasks = []
    CompleteTasks = []
    if len(argv) != 2:
        print("Command takes 2 arguments")
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    res = requests.get(url)
    json = res.json()
    name = json['name']
    url2 = "https://jsonplaceholder.typicode.com/todos"
    req2 = requests.get(url2)
    json2 = req2.json()
    for usr in json2:
        if usr['userId'] == int(argv[1]):
            Tasks.append(usr)
    TasksJSON = []
    json_dict = {}
    for task in Tasks:
        TasksJSON.append({'task': task['title'],
                          'completed': task['completed'],
                          'username': name})
    json_dict = {argv[1]: TasksJSON}
    with open('{}.json'.format(argv[1]), mode="w", encoding="utf-8") as fd:
        json.dump(json_dict, fd)
