from login import Login

def greeting():
    my_login = Login()
    name = my_login.user_availability()
    print(name)


if __name__ == "__main__":
    greeting()