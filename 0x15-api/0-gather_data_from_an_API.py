#!/usr/bin/python3
""" Prove API Rest"""
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
    for task in Tasks:
        if task['completed'] is True:
            CompleteTasks.append(task)
    tt = len(Tasks)
    t = len(CompleteTasks)
    print("Employee {} is done with tasks({}/{}):".format(name, t, tt))
    for task in CompleteTasks:
        print("\t {}".format(task['title']))
