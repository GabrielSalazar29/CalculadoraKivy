class MyScreenModel:
    def __init__(self):
        self._x = ""
        self._y = ""
        self._resultado = ""

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def resultado(self):
        return self._resultado

    @x.setter
    def x(self, valor):
        if self._x == "":
            self._x = valor
        else:
            self._x = str(self._x) + str(valor)
        self.resultado = self._x

    @y.setter
    def y(self, valor):
        self._y = valor

    @resultado.setter
    def resultado(self, valor):
        self._resultado = valor

    def zerar(self):
        self._x = ""
        self._y = ""
        self._resultado = ""
