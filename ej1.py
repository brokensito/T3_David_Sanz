# Creamos la "Torre" con las 3 columnas.
def TorreHanoi(discos, primera, segunda, tercera):

    if discos==1:
        movimiento(discos, primera, tercera)

    else:
        TorreHanoi(discos-1, primera, tercera, segunda)
        movimiento(discos, primera, tercera)
        TorreHanoi(discos-1, segunda, primera, tercera)

    return

def movimiento(discos, primera, tercera):

    return print("Movemos el disco {} de la torre {} a la torre {}.".format(discos,primera,tercera))
    
# Para cualquier numero de discos (n), primero moveremos los discos (n-1) de la torre1  a la torre2.
# Despues, movemos el disco (n) desde la torre1 a la torre3.
# Finalmente, moveremos el resto de discos que se encuentran en la torre2 hacia la torre3.

if __name__=="__main__":

    TorreHanoi(74,"1","2","3")


