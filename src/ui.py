import sys
from rich.console import Console 
from rich.style import Style
from rich.text import Text

class Ui:
    def __init__(self):
        self.console = Console() #console initiation
        self.text = Text() #text initiation

        #Color Schema
        self.completed = self.low = Style(color='#30A14E', bold=True)
        self.archived = self.medium = Style(color="#F0A204", bold=True)
        self.pending = self.high = Style(color="#BD0000",bold=True)
        self.error = self.urgent = Style(color="#FF0011", bold=True)


    

    