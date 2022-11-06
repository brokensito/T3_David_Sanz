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


    def agregar_termino(self, termino, valor):
        aux = Nodo()
        dato = DatoPolinomio(valor, termino)
        aux.info = dato
        if termino > self.grado:
            aux.sig = self.termino_mayor
            self.termino_mayor = aux
            self.grado = termino

        else:
            actual = self.termino_mayor
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def elimina