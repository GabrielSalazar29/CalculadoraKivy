from View.myscreen import MyScreenView


class MyScreenController:

    def __init__(self, model):
        self.model = model
        self.view = MyScreenView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def set_x(self, valor):
        self.model.x = valor

    def get_x(self):
        if self.model.y == "0":
            return self.model.x
        return self.model.y

    def get_y(self):
        return self.model.y

    def set_y(self, valor):

        self.model.y = valor

    def set_operador(self, valor):

        self.model.operador = valor

    def get_operador(self):
        return self.model.operador

    def set_resultado(self):

        self.model.resultado()

    def get_resultado(self):

        return self.model.x

    def get_conta(self):
        return self.model.conta

    def potencia(self):
        self.model.potencia()

    def zerar(self):

        self.model.zerar()

    def apagar(self):

        self.model.apagar()
