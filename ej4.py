class Nodo(object):

    info,sig = None, None

class DatoPolinomio(object):

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

    def eliminar_termino(self, termino):
        aux = self.termino_mayor
        if self.grado == termino:
            self.termino_mayor = aux.sig
            del aux

        else:
            while aux.sig is not None:
                if aux.sig.info.termino == termino:
                    aux.sig = aux.sig.sig
                    del aux.sig
                    return

                aux = aux.sig
                
    def restar(self, nuevo):

        
        return

    def obtener_valor(self, termino):
        aux = self.termino_mayor
        while aux is not None and aux.info.termino > termino:
            aux = aux.sig

        if aux is not None and aux.info.termino == termino:
            return aux.info.valor

        else: 
            return 0

    def imprime(self):

        actual = self.termino_mayor

        while actual is not None:

            print("{} x{}".format(actual.info.valor, actual.info.termino))
            actual= actual.sig



if __name__=="__main__":

    poli1 = Polinomio()
    poli1.agregar_termino(3,3)
    poli1.agregar_termino(2,2)
    poli1.eliminar_termino(3)
    poli1.imprime()