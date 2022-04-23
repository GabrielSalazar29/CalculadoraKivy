class MyScreenModel:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._resultado = 0

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
        self._x = valor
        self.resultado = self._x

    @y.setter
    def y(self, valor):
        self._y = valor

    @resultado.setter
    def resultado(self, valor):
        self._resultado = valor

