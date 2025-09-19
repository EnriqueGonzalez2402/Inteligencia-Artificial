#formateo_cadenas

nombre = 'Juan'
edad = 30

#con f-string
#cadenas dinamicas 
mensaje = f'Hola, me llamo {nombre} y tengo {edad} años.'
print(mensaje)
#metodo format
mensaje = 'Hola, me llamo {} y tengo {} años.'.format(nombre, edad)
print(mensaje)