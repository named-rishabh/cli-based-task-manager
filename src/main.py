from login import Login
import sys
import os
from rich import print
from rich.columns import Columns

def greeting():
    my_login = Login()
    username, name = my_login.user_availability()
    print(f"Welcome, {name}")

    # if len(sys.argv) < 2:
    #     print("Usage: python columns.py DIRECTORY")
    # else:
    #     directory = os.listdir(sys.argv[1])
    #     columns = Columns(directory, equal=True, expand=True)
    #     print(columns)


if __name__ == "__main__":
    greeting()