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

        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while pol1 is not None:
            pol2 = polinomio2.termino_mayor

            while pol2 is not None:

                termino = pol1.info.termino - pol2.info.termino
                valor = pol1.info.valor/pol2.info.valor

                if obtener_valor(paux, termino)!=0:
                    valor+=obtener_valor(paux, termino)
                    obtener_valor(paux, termino, valor)

                else:
                    agregar_termino(paux, termino, valor)

                pol2 = pol2.sig

            pol1=pol1.sig

        return paux
        
        

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

    def existe(self, termino):
        paux = self.termino_mayor

        while paux is not None and paux.info.termino > termino:
            paux = paux.sig

        if paux is not None and paux.info.termino == termino:
            return "El termino {} existe.".format(termino)
        
        else: 
            return "El termino {} NO existe".format(termino)

if __name__=="__main__":

    poli1 = Polinomio()
    poli1.agregar_termino(3,2)
    poli1.agregar_termino(2,2)
    poli1.imprime()

    poli2 = Polinomio()
    poli2.agregar_termino(3,5)
    poli2.agregar_termino(2,4)
    poli2.imprime()

    resta = poli1.restar(poli1,poli2)
    division = poli1.dividir(poli1,poli2)
    eliminar = poli1.eliminar_termino(2)
    existe = poli2.existe(2)

