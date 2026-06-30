import json 
from register import user_input
from rich.console import Console


console = Console()#console initiation

def user_login(): 
    name = ''
    data = user_input('login')
    with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8') as file:
        user_json_data = json.load(file)
        usernames = [user["username"] for user in user_json_data.get("Users")]
        if data[0] in usernames:
            index = usernames.index(data[0])
            if data[1] == user_json_data['Users'][index]['password']:
                name = user_json_data['Users'][index]['name']
            else:
                console.print("Invalid Password", style="#FF0011 bold")
                name = user_login()
                return name
        else:
            console.print('Invalid Credentials', style="#FF0011 bold")
            name = user_login()
            return name
        
        return name

        

def user_availability():
    with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8') as file:
        user_json_data = json.load(file)
        user = [user['username'] for user in user_json_data.get('Users') ]

        if user == ['']:
            user_input('register')
            name = user_login()
            return name
        elif len(user) == 1:
            return (user_json_data.get('Users')[0]['name'])
        else:
            name = user_login()
            return name
    
        

