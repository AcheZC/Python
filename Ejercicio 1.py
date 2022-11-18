"""
DOCSTRING
TITLE:          EJERCICIO 1
AUTHOR:         HUGO DANIEL BUSTAMANTE NIETO
DESCRIPTION:    SCRIPT CONTADOR DE OCURRENCIAS
VERSION:        3.0.2 (Versiones nuevas.Actualizaciones.Correcciones)
NOTA:           DADA UNA PALABARA, DEBERÁ DECIR LAS VECES QUE ESA PALABRA APARECE EN UN PARRAFO CUALQUIERA
GUIA DE ESTILO: PEP8
"""

#Parametros de testeo usados
#La logística Digital es un concepto que surge de la integración entre la logística tradicional y la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando productos físicos, podríamos estar hablando de un golpe devastador para la industria de la logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha introducido las innovaciones digitales.  
#logística

##########################################################################

#Input del usuario
palabra = input('Palabra a buscar: ')
parrafo = input('Parrafo: ')

#Variables
contador = 0 
lisa = []
i = 0
letra = 0
word = ''
ocurrencia = 0
txt = ' ocurrencias encontradas'
length = 0

#Loop para convertir en lista el string del parrafo 
while True:
    try:
        if parrafo[contador]:
            lisa[contador] = parrafo[contador]
            contador += 1
    except IndexError as e:
        break

#Loop para determinar el tamaño del parrafo en lugar de len()
while True:
    try:
        if parrafo[length]:
            length += 1
    except IndexError as e:
        break

#Uso de while para rrecorer el parrafo en vez de for debido a la palabra reservada "in" en el loop 
while i < length: 
    if (((parrafo[i]) == " ") or ((parrafo[i]) == ",") or ((parrafo[i]) == ".")):
        letra = 0
        if word == palabra:
            ocurrencia += 1
        word = ''
    else:
        word = word + parrafo[i]
        letra += 1
    i += 1

print(f'{ocurrencia}{txt}')


##############################################
##Version 1

# palabra = input('Palabra a buscar: ')
# parrafo = input('Parrafo: ')

# ocurrencias = 0

# palabras = []
# palabras = parrafo.split()

# for pal in palabras:
#     if pal == palabra or pal == palabra + ',' or pal == palabra + '.':
#         ocurrencias += 1

# print(str(ocurrencias) + ' Ocurrencias encontradas')

##############################################
##Version 2

# from collections import Counter
# my_str = input('Parrafo: ')
# word = input('Palabra: ')
# counter = Counter(my_str)
# ocurrencias = counter[str(word)]
# print(ocurrencias +  'ocurrencias encontradas')