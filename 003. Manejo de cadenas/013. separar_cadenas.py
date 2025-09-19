#separar_cadenas

#usamos split para poder dividir la cadena en una lista de subcadenas
datos = 'Hola Mundo'
lista = datos.split() # por default se separa todo con espacios
print(lista)

datos = 'Juan,30,México'
lista = datos.split(',')
print(lista)