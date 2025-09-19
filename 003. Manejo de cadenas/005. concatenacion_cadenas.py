#concatenacion_cadenas

#concatenacion de cadenas = union de dos cadenas
# funcion join tambien nos ayuda con eso

cadena1 = 'Hola'
cadena2 = 'Mundo'

#primera forma de concatenar cadenas 
concatenacion = cadena1 + ' ' + cadena2 
print(concatenacion)

#segunda forma de concatenar cadenas con join
concatenacion = ''.join([cadena1, ' ', cadena2])
print(concatenacion)
