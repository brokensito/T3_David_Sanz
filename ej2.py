

# Primero hacemos el determinante de la matrix 3x3 utilizando sarrus unicamente para la longitud dictada.

def determinante(matriz):
    return sarrus(matriz)
    
def sarrus(matriz):
    sumas = (matriz[0][0]*matriz[1][1]*matriz[2][2]) + (matriz[1][0]*matriz[2][1]*matriz[0][2]) + (matriz[0][1]*matriz[1][2]*matriz[2][0])
    restas = (matriz[0][2]*matriz[1][1]*matriz[2][0]) - (matriz[0][1]*matriz[1][0]*matriz[2][2]) - (matriz[0][0]*matriz[1][2]*matriz[2][1])
    return sumas-restas

# Alternativamente, tambien podemos calcular la matriz de forma recursiva para "n" valores y no unicamente para
# una matriz 3x3. Esto se hace mediante el calculo de matriz mediante adjuntos.

# Funcion que devuelve la matriz una vez quitada la fila "i" y la columna "j".
def sacar_adjunto(m, i, j):
    return [fila[:j] + fila[j+1] for fila in (m[:1] + m[i+1:])]


def determinante_rec(matriz):

    # Si la matriz es de 2x2, hacemos calculos simples para sacar el determinante.
    if len(matriz)==2:
        return matriz[0][0]*matriz[1][1]-matriz[1][0]

    suma = 0

    # Bucle para iterar cada columna de la matriz.
    for columna_actual in range(len(matriz)):

        # Calculamos el signo en base al adjunto de la sub-matriz.
        signo = (-1)**(columna_actual)

        # Llamamos de manera recursiva para sacar el determinante de la sub matriz que obtenemos.
        det_submatriz = determinante_rec(sacar_adjunto(matriz, 0, columna_actual))

        # Añadimos el determinante de la submatriz a la suma.
        suma += (signo * matriz[0][columna_actual] * det_submatriz)
    
    return suma

if __name__=="__main__":

    matriz = [
        [8,5,3],
        [5,4,3],
        [6,2,1]
    ]

    determinante(matriz)
    determinante_rec(matriz)