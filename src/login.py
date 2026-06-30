import json 
from register import Register
from ui import Ui

class Login(Ui):
    def __init__(self):
        super().__init__()
        self.register = Register()

    def user_login(self): 
        name = ''
        data = self.register.user_input('login')
        with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8') as file:
            user_json_data = json.load(file)
            usernames = [user["username"] for user in user_json_data.get("Users")]
            if data[0] in usernames:
                index = usernames.index(data[0])
                if data[1] == user_json_data['Users'][index]['password']:
                    name = user_json_data['Users'][index]['name']
                else:
                    self.console.print("Invalid Password", style=self.error)
                    name = self.user_login()
                    return name
            else:
                self.console.print('Invalid Credentials', style=self.error)
                name = self.user_login()
                return name
        
            return name
               

    def user_availability(self):
        with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8')   as file:
            user_json_data = json.load(file)
            user = [user['username'] for user in user_json_data.get('Users') ]

            if user == ['']:
                self.register.user_input('register')
                name = self.user_login()
                return name
            elif len(user) == 1:
                return (user_json_data.get('Users')[0]['name'])
            else:
                name = self.user_login()
                return name
    
        

