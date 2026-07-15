from login import Login
import sys
import os
from rich import print
from rich.columns import Columns
import json

def greeting():
    my_login = Login()
    username, name = my_login.user_availability()
    path = f'./data/{username}.json'
    if os.path.exists(path=path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
    else:
        with open(path, 'w', encoding='utf-8') as file:
            data = {
            "Tasks":{
                "id": "",
                "date": "",
                "time": "",
                "type": "",
                "task": ""
            }}
            
            json.dump(data, file)
       


if __name__ == "__main__":
    greeting()