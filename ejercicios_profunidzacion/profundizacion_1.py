# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

print('Ingrese el primer número de la secuencia:')
# inicio = ....
inicio = int(input())

print('Ingrese el último número de la secuencia:')
# fin = ....
fin = int(input())


# cantidad_numeros ....
cantidad_numeros = 0

# sumatoria ....
sumatoria = 0


# bucle.....
for cantidad_numeros in range(inicio, fin):
    cantidad_numeros += 1

print('la cantidad de num en la secuencia es', cantidad_numeros)


for numero in range(inicio, fin):
    sumatoria += numero



print('la suma de los num de la secuencia es', sumatoria + fin)



# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros
# Imprimir resultado en pantalla

promedio = (sumatoria + fin) / cantidad_numeros
print('promedio:',promedio)

