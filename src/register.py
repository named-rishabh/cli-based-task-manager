import json
import sys
from rich.console import Console

console = Console()

def data_parser(data): 
    with open('CLI_Based_Task_Manager/data/user.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

def user_input(purpose):
     #Ui window initiation
    console.print("Enter Username: ", style='#30A14E bold')
    username = sys.stdin.readline().strip()

    if purpose == 'register':    
        console.print("Enter Name: ", style='#30A14E bold')
        name = sys.stdin.readline().strip()
        console.print("Enter Password: ", style='#30A14E bold')
        password = sys.stdin.readline().strip()

        verify_registering_user(username, name, password)
    else:
        console.print("Enter Password: ", style='#30A14E bold')
        password = sys.stdin.readline().strip()
        return(username, password)



def verify_registering_user(username, name, password, ):
    with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8') as file:
        user_json_data = json.load(file)
        user = [user['username'] for user in user_json_data.get('Users') ]
        if username in user:
            console.print("Username Already Exists!", style='#FF0011 bold')
            user_input('register')
        elif user == ['']:
            register(username, name, password, 'w')
        else:
            register(username, name, password, 'a')


def register(username, name, password, code):
    data = {
        "username": f'{username}',
        "name": f"{name}",
        "password": f"{password}"
    }

    if code == "w":
        user_data = {"Users" : [data]}
        data_parser(user_data)
    elif code == "a":
        with open('CLI_Based_Task_Manager/data/user.json', '+rt', encoding='utf-8') as file:
            user_json_data = json.load(file)
            user_data = user_json_data['Users'].append(data)
            data_parser(user_json_data)
            

