import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen


class MyScreenView(MDScreen):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)

    def set_x(self, valor):
        self.controller.set_x(valor)
        self.ids.resultado.text = str(self.controller.get_x())

    def set_y(self, valor):
        self.controller.set_y(valor)

    def set_resultado(self, valor):
        self.controller.set_resultado(valor)

    def zerar(self):
        self.controller.zerar()
        self.ids.resultado.text = str(0)


Builder.load_file(os.path.join(os.path.dirname(__file__), "myscreen.kv"))