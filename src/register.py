import json
import sys
from ui import Ui

class Register(Ui):
    def __init__(self):
        self.UI = Ui()
        self.console = self.UI.console
        
    def data_parser(self, data):  
        with open('CLI_Based_Task_Manager/data/user.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def user_input(self, purpose):    
     #Ui window initiation
        self.console.print("Enter Username: ", style='#30A14E bold')
        username = sys.stdin.readline().strip()

        if purpose == 'register':    
            self.console.print("Enter Name: ", style='#30A14E bold')
            name = sys.stdin.readline().strip()
            self.console.print("Enter Password: ", style='#30A14E bold')
            password = sys.stdin.readline().strip()

            self.verify_registering_user(username, name, password)
        else:
            self.console.print("Enter Password: ", style='#30A14E bold')
            password = sys.stdin.readline().strip()
            return(username, password)



    def verify_registering_user(self, username, name, password ):
        with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8') as file:
            user_json_data = json.load(file)
            user = [user['username'] for user in user_json_data.get('Users') ]
            if username in user:
                self.console.print("Username Already Exists!", style='#FF0011 bold')
                self.user_input('register')
            elif user == ['']:
                self.register(username, name, password, 'w')
            else:
                self.register(username, name, password, 'a')


    def register(self, username, name, password, code):
        data = {
            "username": f'{username}',
            "name": f"{name}",
            "password": f"{password}"
        }

        if code == "w":
            user_data = {"Users" : [data]}
            self.data_parser(user_data)
        elif code == "a":
            with open('CLI_Based_Task_Manager/data/user.json', '+rt', encoding='utf-8') as file:
                user_json_data = json.load(file)
                user_data = user_json_data['Users'].append(data)
                self.data_parser(user_json_data)
            

