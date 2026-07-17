from textual.app import App, ComposeResult
from textual.app import RenderResult, ComposeResult, App
from textual.widget import Widget
from textual.widgets import Label, Header
from main import Main

# class Name(Widget):

#     def render(self) -> RenderResult:
#         return f"{self.get_name}"

#     def get_name(self):
#         name = greeting()
#         return name

class Layout(App):
    main = Main()
    username = main.greeting()
    TITLE = 'Task Manager'
    SUB_TITLE = f"{username}"
        

    def compose(self) -> ComposeResult:
        yield Header()

    

if __name__ == "__main__":
    app = Layout()
    app.run()