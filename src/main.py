from login import Login
import sys
import os
from rich import print
from rich.columns import Columns
import json

class Main:
    def __init__(self):
        self.greeting()
        self.check_avaibility_of_file_for_user_task(self.username)

    def check_avaibility_of_file_for_user_task(self, username):
        self.path = f'./data/{username}.json'
        if os.path.exists(path=self.path):
            with open(self.path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                print(self.data)
        else:
            with open(self.path, 'w', encoding='utf-8') as file:
                self.data = {
                "Tasks":[{
                "id": "",
                "date": "",
                "time": "",
                "type": "",
                "task": "",
                "status": ""
                }]}
            
                json.dump(self.data, file)

    def greeting(self):
        self.my_login = Login()
        self.username, self.name = self.my_login.user_availability()

        return self.name