def crearmatriz():
    listaa = []
    fila = int(input())
    columna = int(input())
    if fila > 0 and columna > 0: 
        for i in range(fila):
            listaa.append([])
            for j in range(columna):
                n = int(input())
                listaa[i].append(n)
    else: 
        print('Error')
    return listaa

def main():
    matriz = crearmatriz()
    listaa_col = []
    if len(matriz) > 0:
        for i in range(len(matriz[0])):
            count = 0
            for j in range(len(matriz)):
                count += matriz[j][i] 
            listaa_col.append(count)
        print(listaa_col)
if __name__=='__main__':
    main()

