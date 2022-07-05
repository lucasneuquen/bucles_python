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
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from ipaddress import summarize_address_range


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

operacion='inicio'
verificador=0

while operacion!='fin':
    
    num1 = int(input('Ingrese el primer número:\n'))
    num2= int(input('Ingrese el segundo número:\n'))
    
    while verificador!=1:
        operacion=input('ingrese el símbolo de la cuenta que desea realizar o FIN si desea salir de la aplicación:\n')
        if operacion=='+':
            verificador=1
            cuenta='suma'
            resultado=num1+num2
        elif operacion=='-':
            verificador=1
            cuenta='resta'
            resultado=num1-num2
        elif operacion=='*':
            verificador=1
            cuenta='multiplicación'
            resultado=num1*num2
        elif operacion=='/':
            verificador=1
            cuenta='división'
            resultado=num1/num2
        elif operacion=='**':
            verificador=1
            cuenta='potencia'
            resultado=num1**num2
        elif operacion=='fin':
            verificador=1
            
        else:
            print('el valor ingresado no es válido. Por favor vuelva a intentarlo.')
    
    
    verificador=0

    if operacion!='fin':
        print('el calculo de', cuenta, ' deseado con los números ingresados es: ',resultado)


print('usted a salido correctamente del sistema')