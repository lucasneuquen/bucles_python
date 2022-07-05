# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
print('************************')
# Empezar aquí la resolución del ejercicio

    
# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable
sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

for i in notas:
    if i>0:
        sumatoria=sumatoria+i
        cantidad_notas+=1
    else:
        cantidad_ausentes+=1

# ***** print(sumatoria,cantidad_notas, cantidad_ausentes)

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

# Terminado el bucle calcule el promedio como
promedio = sumatoria / cantidad_notas

# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado
if promedio>=90:
    letra='A'
elif promedio>=80:
    letra='B'
elif promedio>=70:
    letra='C'
elif promedio>=60:
    letra='D'
else:
    letra='F'
# Imprima en pantalla al cantidad de ausentes
print('Según sus notas obtuvo la siguiente calificación: ',letra, ', con un promedio de: ', promedio)
print('total de encuentros ausentes: ', cantidad_ausentes)

print('****fin del informe***')