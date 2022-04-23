from kivymd.app import MDApp
from Controller.myscreen import MyScreenController
from Model.myscreen import MyScreenModel


class CalculadoraApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = MyScreenModel()
        self.controller = MyScreenController(self.model)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return self.controller.get_screen()


CalculadoraApp().run()
