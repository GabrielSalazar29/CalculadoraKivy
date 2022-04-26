import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen


class MyScreenView(MDScreen):
    controller = ObjectProperty()
    model = ObjectProperty()

    def set_x(self, valor):
        self.controller.set_x(valor)
        self.ids.resultado.text = f"[b]{self.controller.get_x()}[/b]"

    def set_y(self, valor):
        self.controller.set_y(valor)

    def set_operador(self, valor):
        self.controller.set_operador(valor)
        self.ids.contaparc.text = f"{self.controller.get_x()} {self.controller.get_operador()}"
        self.ids.resultado.text = "[b]0[/b]"

    def set_resultado(self):
        self.controller.set_resultado()
        self.ids.contaparc.text = self.controller.get_conta()
        self.ids.resultado.text = f"[b]{self.controller.get_resultado()}[/b]"

    def zerar(self):
        self.controller.zerar()
        self.ids.resultado.text = "[b]0[/b]"
        self.ids.contaparc.text = ""

    def apagar(self):
        self.controller.apagar()
        if self.controller.get_x() == "":
            self.ids.resultado.text = f"[b]0[/b]"
        elif self.controller.get_y() == "" and self.controller.get_operador() != "":
            self.ids.resultado.text = f"[b]0[/b]"
        else:
            self.ids.resultado.text = f"[b]{self.controller.get_x()}[/b]"

        if "=" in self.ids.contaparc.text:
            self.ids.contaparc.text = ""


Builder.load_file(os.path.join(os.path.dirname(__file__), "myscreen.kv"))
