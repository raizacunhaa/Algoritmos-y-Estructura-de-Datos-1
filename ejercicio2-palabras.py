
def ingresar_palabras():
    palabras = []
    cant= int(input("Cantidad de palabras que desea ingresar: "))
    for x in range(cant):
        pal = input("Ingrese una palabra: ")
        palabras.append(pal)
    return palabras

def encontrar_palabras_con_letra(palabras,letra):
    palabras_con_letra = []
    posicion_letra = 0
    posicion_pal = 0
    for pal in palabras:
        for letra_pal in pal:
            posicion_letra = 0
            if letra_pal==letra:
                palabras_con_letra.append(palabras[posicion_letra+posicion_pal])
                posicion_letra = posicion_letra + 1
        posicion_pal = posicion_pal + 1
    print('Lista de palabras con la letra seleccionada', palabras_con_letra)
    return palabras_con_letra
    
def ordenar_palabras_longitud(palabras):
    for y in range (len(palabras)-1):
        for x in range (len(palabras)-1):
            if len(palabras[x]) > len(palabras[x+1]):
                auxiliar = palabras[x+1]
                palabras[x+1] = palabras[x]
                palabras[x] = auxiliar
    print('Lista de palabras ordenadas por longitud', palabras)
    return palabras

#Bloque principal
palabras = ingresar_palabras()
letra = input("Ingrese la letra que quiere buscar: ")
palabras_con_letra = encontrar_palabras_con_letra(palabras, letra)
palabras_ordenadas_por_longitud = ordenar_palabras_longitud(palabras)

