import sys
from rich.console import Console 
from rich.style import Style
from rich.text import Text
from login import user_availability

class Ui:
    def __init__(self):
        console_init = Console()
        self.console = console_init #console initiation

        #Color Schema
        self.completed = self.low = Style(color='#30A14E', bold=True)
        self.archived = self.medium = Style(color="#F0A204", bold=True)
        self.pending = self.high = Style(color="#BD0000",bold=True)
        self.error = self.urgent = Style(color="#FF0011", bold=True)


    def greetings(self):
        name = user_availability()
        print(name)

if __name__ == "__main__":
    window = Ui()
    window.greetings()