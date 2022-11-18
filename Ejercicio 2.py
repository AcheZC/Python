"""
DOCSTRING
TITLE:          EJERCICIO 2
AUTHOR:         HUGO DANIEL BUSTAMANTE NIETO
DESCRIPTION:    PRIORITY SORTER
VERSION:        0.0.5 (Versiones nuevas.Actualizaciones.Correcciones)
NOTA:           DADO UN ARREGLO DE ENTRADA, ORDENAR POR PRIORIDAD UNICAMENTE LOS ELEMENTOS QUE CUMPLEN LOS CRITERIOS ESTABLECIDOS
GUIA DE ESTILO: PEP8
"""

#Parametros de testeo usados

# criteria1 = [
# ('weight', '=', 3)
# ]

# criteria2 = [
# ('width', '>=', 2),
# ('length', '<=', 20),
# ]

##########################################################################

# Entry Tipo lista de diccionarios
entry = [
{'id': 12340, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
125, 'priority': 2},
{'id': 12341, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
127, 'priority': 4},
{'id': 12342, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
129, 'priority': 6},
{'id': 12343, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
131, 'priority': 0},
{'id': 12344, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
133, 'priority': 0},
{'id': 12345, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
135, 'priority': 0},
{'id': 12346, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
137, 'priority': -1},
{'id': 12347, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
139, 'priority': 0},
{'id': 12348, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
141, 'priority': 2},
{'id': 12349, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
143, 'priority': 0},
{'id': 12350, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
145, 'priority': 0},
{'id': 12351, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
147, 'priority': 10},
{'id': 12352, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
149, 'priority': 0},
{'id': 12353, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
151, 'priority': 0},
{'id': 12354, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
153, 'priority': 0},
{'id': 12355, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
155, 'priority': 0},
{'id': 12356, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
157, 'priority': 0},
{'id': 12357, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
159, 'priority': 0},
{'id': 12358, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
161, 'priority': 0},
{'id': 12359, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
135, 'priority': 0},
{'id': 12360, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
137, 'priority': 0},
{'id': 12361, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
139, 'priority': 0},
{'id': 12362, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost':
141, 'priority': -2},
{'id': 12363, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost':
153, 'priority': -2},
{'id': 12364, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
145, 'priority': -6},
{'id': 12366, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
147, 'priority': 0},
{'id': 12367, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
149, 'priority': 0},
{'id': 12365, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
151, 'priority': 2},
{'id': 12368, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
181, 'priority': 2},
{'id': 12369, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
183, 'priority': 0},
]

criteria1 = [
('weight', '=', 3)
]

criteria2 = [
('width', '>=', 2),
('length', '<=', 20),
]

def recorreParametros(criterio, entrada):
    """
    DOCSTRING
    TITLE:          RECORREPARAMETROS
    AUTHOR:         HUGO DANIEL BUSTAMANTE NIETO
    DESCRIPTION:    RECORRE LOS PARAMETROS DADOS 
    VERSION:        0.0.0 (Versiones nuevas.Actualizaciones.Correcciones)
    NOTA:           DADO UN ARREGLO DE ENTRADA, Y LOS CRITERIOS DE ORDENACIÓN GUARDA LOS CRITERIOS EN VARIABLES Y SEPARA LA ENTRADA 
                    EN 2 LISTAS SEGUN LOS CRITERIOS
    PARAMETROS:     CRITERIO, ENTRADA
    """

    #Variables de criterios contadores y listas a retornar
    var1, var2, var3, var4 = 0, 0, 0, 0
    operador1, operador2, operador3, operador4 = 0, 0, 0, 0
    val1, val2, val3, val4 = 0, 0, 0, 0
    contadict, contador = 0, 0
    listordenar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    listanormal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    #Recorremos la lista del criterio
    for i in criterio:
        if contador == 0: 
            var1 = i[0]
            operador1 = i[1]
            val1 = i[2]
        elif contador == 1:
            var2 = i[0]
            operador2 = i[1]
            val2 = i[2]
        elif contador == 2:
            var3 = i[0]
            operador3 = i[1]
            val3 = i[2]
        elif contador == 3:
            var4 = i[0]
            operador4 = i[1]
            val4 = i[2]
        contador += 1

#################################################################################################

    # #Obtener cuantos tuplas hay en el criterio de ordenación
    # if var1 != "":
    #     if var2 != "":
    #         if var3 != "":
    #             if var4 != "":
    #                 return (var4, operador4, val4), (var3, operador3, val3), (var2, operador2, val2), (var1, operador1, val1)
    #             return (var3, operador3, val3), (var2, operador2, val2), (var1, operador1, val1)
    #         return (var2, operador2, val2), (var1, operador1, val1)
    #     return (var1, operador1, val1)
    
    # Separa en 2 listas - SE PUEDE HACER FUNCION PARA EVITAR REPETIR EL CODIGO CON MAS TIEMPO
    # Recorre la entrada entera
    for dic in entrada:
        #Recorre los diccionarios uno a uno
        for key in dic:
            #SE PUEDE RESUMIR A TRAVES DE CREAR FUNCION CON MAS TIEMPO
            #Compara los keys contra los criterios de ordenacion dados
            if key == var1:
                    if operador1 == '=':
                        if dic[key] == val1:
                            #Agregamos los diccionarios que cumplen los criterios a la lista a ordenar 
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador1 == '>=':
                        if dic[key] >= val1:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador1 == '<=':
                        if dic[key] <= val1:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador1 == '<':
                        if dic[key] <= val1:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador1 == '>':
                        if dic[key] <= val1:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
            if key == var2:
                    if operador2 == '=':
                        if dic[key] == val2:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador2 == '>=':
                        if dic[key] >= val2:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador2 == '<=':
                        if dic[key] <= val2:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador2 == '<':
                        if dic[key] <= val2:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador2 == '>':
                        if dic[key] <= val2:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
            if key == var3:
                    if operador3 == '=':
                        if dic[key] == val3:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador3 == '>=':
                        if dic[key] >= val3:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador3 == '<=':
                        if dic[key] <= val3:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador3 == '<':
                        if dic[key] <= val3:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador3 == '>':
                        if dic[key] <= val3:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
            if key == var4:
                    if operador4 == '=':
                        if dic[key] == val4:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador4 == '>=':
                        if dic[key] >= val4:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador4 == '<=':
                        if dic[key] <= val4:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador4 == '<':
                        if dic[key] <= val4:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
                    elif operador4 == '>':
                        if dic[key] <= val4:
                            listordenar[contadict] = dic
                            break
                        else:
                            listanormal[contadict] = dic
                            break
        
        #Cuenta cuantos diccionarios hay para poder agregar el diccionario al indice de la lista actual
        contadict += 1
    
    #Se retornan las listas divididas para ordenar
    return(listordenar, listanormal)

#Funcion de separación de listas  
def junta(listas):
    """
    DOCSTRING
    TITLE:          JUNTA Y ORDENA LAS LISTAS E IMPRIME UN OUTPUT
    AUTHOR:         HUGO DANIEL BUSTAMANTE NIETO
    DESCRIPTION:    SELECCIONA LAS LISTAS Y LAS UNE EN ORDEN 
    VERSION:        0.0.0 (Versiones nuevas.Actualizaciones.Correcciones)
    NOTA:           DADAS LAS LISTAS ORDENA LISTAORDENAR Y LA UNE CON LISTA NORMAL PARA FORMAR EL OUTPUT A MOSTRAR
    PARAMETROS:     LISTAORDENAR, LISTANORMAL
    """

    #Variables
    lisordenar = listas[0]
    lisnormal = listas[1]
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    lisout = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    conta = 0
    containdice = 0

    # print(listas[0])

    #Recorre la lista
    for i in lisordenar:

        #Si indice en la lista no es diccionario:
        if i in nums:
            continue
        else:
            #Recorre el diccionario 
            for key in i: 
                if 'priority' in key:
                    lisordenar[conta] = i
            containdice += 1
        conta += 1

    ##################################################################################ORDENAR pasando la lista lisordenar

    #Setea a 0 los contadores de nuesvo
    conta = 0
    containdice = 0

    #Recorrer la lista normal
    for i in lisnormal:
        if i in nums:
            continue
        else:
            #Recorre el diccionario 
            for key in i: 
                if 'priority' in key:
                    lisnormal[conta] = i
                    # print(lisnormal[conta])

            containdice += 1
        conta += 1
    print(ordena(lisordenar))

def ordena(lista):
    """
    DOCSTRING
    TITLE:          ORDENA LAS LISTAS Y RETORNA EN ORDEN
    AUTHOR:         HUGO DANIEL BUSTAMANTE NIETO
    DESCRIPTION:    ANALIZA EL PRIORITY Y MUEVE LOS DICCIONARIOS DE MAYOR A MENOS 
    VERSION:        0.0.1 (Versiones nuevas.Actualizaciones.Correcciones)
    NOTA:           DADAS LA LISTA ORDENA LISTAORDENAR
    PARAMETROS:     LISTAORDENAR
    """
    contlisa = 0
    contindex = 0
    previous = 0
    cont = 10

    while cont >= 0:
        contlisa= 0
        contindex = 0
        previous = 0

        for dic in lista:
            try:
                for key in dic:
                        if key == 'priority':
                            # previous = previous + key
                            a = dic[key] #YA ACCEDIMOS AL VALOR
                            #Revisamos que el valor actual en priority sea menor que el anterior 
                            if a >= previous:
                                #Intercambiamos los valores de los diccionarios  
                                indice = contindex - 1
                                # b = lista[indice] # b = dic[key +1]
                                # c = lista[contindex]                    
                                lista[indice], lista[contindex] = lista[contindex], lista[indice]
                            contindex += 1
            except:
                continue
            previous = a
            # print(a)
            contlisa += 1
        cont -= 1
    
    return(lista) #print(lista)
    

junta(recorreParametros(criteria2, entry))

