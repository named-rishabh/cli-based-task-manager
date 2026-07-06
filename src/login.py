import json 
from register import Register
from ui import Ui

class Login(Ui):
    def __init__(self):
        super().__init__()
        self.UI = Ui()
        self.console = self.UI.console
        self.register = Register()

    def user_login(self): 
        data = self.register.user_input('login')
        with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8') as file:
            user_json_data = json.load(file)
            usernames = [user["username"] for user in user_json_data.get("Users")]

            if (data[0] in usernames) and (data[1] == user_json_data['Users'][usernames.index(data[0])]['password']):
                index = usernames.index(data[0])
                username, name = user_json_data['Users'][index]['username'], user_json_data['Users'][index]['name']
                
            else:
                self.console.print('Invalid Credentials', style=self.error)
                username, name = self.user_login()
                return (username, name)
        
            return (username, name)
               

    def user_availability(self):
        with open('CLI_Based_Task_Manager/data/user.json', 'r', encoding='utf-8')   as file:
            user_json_data = json.load(file)
            user = [user['username'] for user in user_json_data.get('Users')]

            if user == ['']:
                self.register.user_input('register')
                username, name = self.user_login()
                return (username, name)
            elif len(user) == 1:
                return ( user_json_data.get('Users')[0]['username'],user_json_data.get('Users')[0]['name'])
            else:
                username, name = self.user_login()
                return (username, name)
    
        

