from login import Login
import sys
import os
from rich import print
from rich.columns import Columns

def greeting():
    my_login = Login()
    username, name = my_login.user_availability()
    print(f"Welcome, {name}")


if __name__ == "__main__":
    greeting()