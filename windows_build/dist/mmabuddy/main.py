import webbrowser
from manager import Manager


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform



class browserLaunch:
    url = None

    def __init__(self, u):
        self.url = u

    def launch(self):
        webbrowser.open_new_tab(self.url)


class MMABuddyApp(App):

    man = None



    def build(self):
        self.icon = "logo.png"
        Window.size = (500, 600)
        inner_layout = GridLayout(size_hint_y=None, cols=1)
        inner_layout.bind(minimum_height=inner_layout.setter('height'))

        self.man = Manager()
        self.man.update_cards()
        for card in self.man.upcoming_cards:
            btn = Button(text=card.__str__(), size_hint_y=None, size=(Window.width, 75),halign="left")
            bl = browserLaunch(card.link)
            btn.on_press=bl.launch
            inner_layout.add_widget(btn)

        root = ScrollView()

        root.add_widget(inner_layout)

        return root

    def on_request_close(self, *args):
        self.man.kill_thread()
        return True

if __name__ == '__main__':
    MMABuddyApp().run()


