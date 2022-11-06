from operator import attrgetter

class Nave():

    # Utilizamos **naves para asi poder pasar los atributos de las naves en cualquier orden.

    def __init__(self, **naves):
        self.nombre = naves["n"]
        self.largo = naves["l"]
        self.tripulacion = naves["t"]
        self.pasajeros = naves["p"]

    def mostrar(self):
        return print("Nombre = {}\nLargo = {}\nTripulacion = {}\nPasajeros = {}".format(self.nombre, self.largo, self.tripulacion, self.pasajeros))
    

def nombre_listas(lista, nave):
    for i in lista:
        if nave in i.nombre:
            return i.mostrar()


def comienzo_lista(lista,comienzo):
    nombres = []
    for i in lista:
        if i.nombre[:2]==comienzo:
            nombres.append(i.nombre)
    return nombres

def pasajeros_lista(lista, cantidad):
    nombres = []
    for i in lista:
        if i.pasajeros>=cantidad:
            nombres.append(i.nombre)

    return nombres
        

if __name__=="__main__":

    # Creamos una lista de naves
    lista = [
        Nave(n="Halcon Milenario YT-1300", l=35, t=40, p=10),
        Nave(n="Estrella de la Muerte", l=160000, t=1000000, p=100000),
        Nave(n="Caza TIE", l=6, t=1, p=0),
        Nave(n="AT-AT", l=44, t=3, p=40),
        Nave(n="AT-ST", l=9, t=2, p=0)
        ]

    # Ordenamos por nombre de manera ascendiente y por largo de manera descendiente.
    nombre = sorted(lista,key=attrgetter("nombre"))
    lista_nombres = [x.nombre for x in nombre]
    
    largo = sorted(lista, key=attrgetter("largo"), reverse=True)
    lista_largo =[x.nombre for x in largo]

    # Mostrar la informacion de Halcon Milenario y Estrella de la Muerte.
    nombre_listas(lista, "Halcon Milenario")
    nombre_listas(lista, "Estrella de la Muerte")

    # Determinar cuales son las cinco naves con mayor cantidad de pasajeros.
    pasajeros = sorted(lista, key=attrgetter("pasajeros"), reverse=True)
    lista_pasajeros = [x.nombre for x in pasajeros[:4]]

    # Indicar cual es la nave que requiere mayor cantidad de tripulacion.
    ## Ordenamos las naves segun la tripulacion y luego usamos el "attrgetter" para clasificar por pasajeros de mayor a menor.
    ### Despues, cogemos el nombre de la primera nave, es decir, la nave con mayor numero de tripulantes.
    tripulacion = sorted(lista, key=attrgetter("tripulacion"), reverse=True)
    max_tripulacion = [x.nombre for x in tripulacion[0]]
    
    # Mostrar todas las naves que comienzan con AT
    ## Utilizamos la funcion comienzo_lista para ver si los caracteres dados coinciden con el comienzo de los nombres en la lista.
    comienzo_lista(lista, "AT")

    # Listar todas las naves que pueden llevar seis o mas pasajeros.
    pasajeros_lista(lista, 6)

    # Listar toda la informacion de la nave mas pequeña y la mas grande.
    ## Utilizamos un bucle para sacar la primera y ultima nave de la nueva lista ordenada por longitud.
    ordenar = sorted(lista, key=attrgetter("largo"))
        
    for i in range(len(lista)):
        if i==0:
            ordenar[i].mostrar()

        elif i==(len(lista)-1):
            ordenar[i].mostrar()




    
