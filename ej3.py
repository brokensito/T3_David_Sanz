class Nodo(objeto):

    info,sig = None, None

class DatoPolinomio(objeto):

    def __init__(self, valor, termino):
        self.valor = valor 
        self.termino = termino

class Polinomio(DatoPolinomio):

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1