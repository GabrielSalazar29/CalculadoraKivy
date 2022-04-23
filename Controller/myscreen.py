from View.myscreen import MyScreenView

class MyScreenController:

    def __init__(self, model):
        self.model = model
        self.view = MyScreenView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def set_x(self, valor):
        self.model.x = valor

    def set_y(self, valor):

        self.model.y = valor

    def set_resultado(self, valor):

        self.model.resultado = valor