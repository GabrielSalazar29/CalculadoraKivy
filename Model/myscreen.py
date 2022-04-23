class MyScreenModel:
    def __init__(self):
        self._x = ""
        self._y = ""
        self._operador = ""
        self._resultado = ""

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def operador(self):
        return self._operador

    @x.setter
    def x(self, valor):

        if self._operador == "":
            if self._x == "":
                self._x = valor
            else:
                self._x = str(self._x) + str(valor)
        else:
            if self._y == "":
                self._y = valor
            else:
                self._y = str(self._y) + str(valor)

    @operador.setter
    def operador(self, valor):
        self._operador = valor

    def resultado(self):
        if self._operador == "+":
            self._resultado = float(self._x) + float(self._y)
            self._x = self._resultado
            self._y = ""
        elif self._operador == "-":
            self._resultado = float(self._x) - float(self._y)
            self._x = self._resultado
            self._y = ""
        elif self._operador == "x":
            self._resultado = float(self._x) * float(self._y)
            self._x = self._resultado
            self._y = ""
        elif self._operador == "/":
            self._resultado = float(self._x) / float(self._y)
            self._x = self._resultado
            self._y = ""

        return self.resultado

    def zerar(self):
        self._x = ""
        self._y = ""
        self._operador = ""
        self._resultado = ""
