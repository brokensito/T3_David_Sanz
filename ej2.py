
def determinante(matriz):
    return sarrus(matriz)
    
def sarrus(matriz):
    sumas = (matriz[0][0]*matriz[1][1]*matriz[2][2]) + (matriz[1][0]*matriz[2][1]*matriz[0][2]) + (matriz[0][1]*matriz[1][2]*matriz[2][0])
    restas = (matriz[0][2]*matriz[1][1]*matriz[2][0]) - (matriz[0][1]*matriz[1][0]*matriz[2][2]) - (matriz[0][0]*matriz[1][2]*matriz[2][1])
    return sumas-restas

def determinante_rec(matriz):


    pass

if __name__=="__main__":

    matriz = [
        [8,5,3],
        [5,4,3],
        [6,2,1]
    ]

    determinante(matriz)