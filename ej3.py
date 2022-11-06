class Nave():

    # Utilizamos **naves para asi poder pasar los atributos de las naves en cualquier orden.

    def __init__(self, **naves):
        self.nombre = naves["n"]
        self.largo = naves["l"]
        self.tripulacion = naves["t"]
        self.pasajeros = naves["p"]

    def mostrar(self):
        return print("Nombre = {}\nLargo = {}\nTripulacion = {}\nPasajeros = {}".format(self.nombre, self.largo, self.tripulacion, self.pasajeros))
    
def nombre_lista(lista, valor):
    for i in range(len(lista)):
        if valor in lista[i].nombre:
            return lista[i].mostrar()
    else:
        return print("La nave que intentas consultar no esta dentro de nuestra base de datos, intentalo de nuevo.")

def comienzo_lista(lista,comienzo):
    nombres = []
    for i in range(len(lista)):
        if lista[i].nombre[:2]==comienzo:
            nombres.append(lista[i].nombre)
    return nombres

def ord_nombre(valor):
    return valor.nombre




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

    # Mostrar la informacion de Halcon Milenario y Estrella de la Muerte.
    nombre_lista(lista, "Halcon Milenario")
    nombre_lista(lista, "Estrella de la Muerte")

    # Determinar cuales son las cinco naves con mayor cantidad de pasajeros.



    # Indicar cual es la nave que requiere mayor cantida de tripulacion.
    
    # Mostrar todas las naves que comienzan con AT
    ## Utilizamos la funcion comienzo_lista para ver si los caracteres dados coinciden con el comienzo de los nombres en la lista.
    comienzo_lista(lista, "AT")

    



    
