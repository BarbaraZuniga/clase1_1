#Arreglo unidimensionales (lista)
#definir de una lista
numeros =[1,2,3,4,5]
#imprimir la lista
print("Lista de números", numeros)
#acceso a elementos individuales de la lista
print("Lista de números", numeros[0]) #los indices comienzan con 0
print("Lista de números", numeros[-1]) #accede al ultimo elemento

#operaciones básicas de lista
#agregar un elemento al final de la lista
numeros.append(6)
print("Lista despúes de agregar 6:", numeros)

#eliminar un elemento de la lista
numeros.remove(2)
print("Lista despúes de eliminar 2:", numeros)
#eliminar un elemento de la lista por indice
numeros.pop(0)
print("Lista despúes de eliminar 4:", numeros)
#longitud de la lista
print("Longitud de la lista",len(numeros))
