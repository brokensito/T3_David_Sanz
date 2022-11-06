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


    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()
        dato = DatoPolinomio(valor, termino)
        aux.info = dato
        if termino > polinomio.grado:
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino

        else:
            actual = polinomio.termino_mayor
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

    def restar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado+1):
            total = obtener_valor(polinomio1, i) - obtener_valor(polinomio2, i)
            if total !=0:
                agregar_termino(paux,i, total)
        return paux

    def dividir(polinomio1, polinomio2):

        paux = 
        
        

    def obtener_valor(polinomio, termino):
        aux = polinomio.termino_mayor
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
    poli1.agregar_termino(3,2)
    poli1.agregar_termino(2,2)
    poli1.eliminar_termino(3)
    poli1.imprime()