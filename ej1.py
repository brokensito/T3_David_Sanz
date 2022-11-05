
def TorreHanoi(discos, primera, segunda, tercera):

    if discos==1:
        print("Movemos el disco 1 de la torre {} a la torre {}.".format(primera,tercera))

    else:
        TorreHanoi(discos-1, primera, tercera, segunda)
        print("Movemos el disco {} de la torre {} a la torre {}.".format(discos,primera,tercera))
        TorreHanoi(discos-1, segunda, primera, tercera)

    return


if __name__=="__main__":
    
    TorreHanoi(74,"1","2","3")


