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

    def set_operador(self, valor):
        self.controller.set_operador(valor)
        self.ids.contaparc.text = f"{self.controller.get_x()} {self.controller.get_operador()}"
        self.ids.resultado.text = str(0)

    def set_resultado(self):
        self.controller.set_resultado()
        self.ids.contaparc.text = ""
        self.ids.resultado.text = f"{self.controller.get_resultado()}"

    def zerar(self):
        self.controller.zerar()
        self.ids.resultado.text = str(0)
        self.ids.contaparc.text = ""


Builder.load_file(os.path.join(os.path.dirname(__file__), "myscreen.kv"))