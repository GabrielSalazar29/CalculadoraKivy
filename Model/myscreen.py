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
        valor = str(valor)
        if self._operador == "":
            if self._x == "":
                if valor == ".":
                    self._x = "0."
                else:
                    self._x = valor
            else:
                if "." in self._x and valor == ".":
                    valor = ""
                self._x = self._x + valor
        else:
            if self._y == "":
                if valor == ".":
                    self._y = "0."
                else:
                    self._y = valor
            else:
                if "." in self._y and valor == ".":
                    valor = ""
                self._y = self._y + valor

    @operador.setter
    def operador(self, valor):
        self._operador = valor

    def resultado(self):

        self._x = str(self._x)
        if self._y == "":
            self._y = "0"
        self._y = str(self._y)

        if len(self._x) >= 2:
            if self._x[-1] == "0" and self._x[-2] == ".":
                self._x = int(self._x[:-2])
            elif "." in self._x:
                self._x = float(self._x)
            else:
                self._x = int(self._x)
        else:
            self._x = int(self._x)

        if len(self._y) >= 2:
            if self._y[-1] == "0" and self._y[-2] == ".":
                self._y = int(self._y[:-2])
            elif "." in str(self._y):
                self._y = float(self._y)
            else:
                self._y = int(self._y)
        else:
            self._y = int(self._y)

        if self._operador == "+":
            self._resultado = self._x + self._y
            self._x = self._resultado
            self._y = ""
        elif self._operador == "-":
            self._resultado = self._x - self._y
            self._x = self._resultado
            self._y = ""
        elif self._operador == "x":
            self._resultado = self._x * self._y
            self._x = self._resultado
            self._y = ""
        elif self._operador == "/":
            self._resultado = self._x / self._y
            self._x = self._resultado
            self._y = ""

        self._operador = ""

    def zerar(self):
        self._x = ""
        self._y = ""
        self._operador = ""
        self._resultado = ""

    def apagar(self):
        self._x = str(self._x)
        self._y = str(self._y)

        if self._operador == "":
            self._x = self._x[:-1]
        else:
            self._y = self._y[:-1]

