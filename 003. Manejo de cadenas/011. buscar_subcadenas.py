#buscar_subcadenas

#find busca subcadenas 
#si hubiera varios "mundos" es cadena solo arrojaria el indice del primer mundo
cadena = 'Hola, mundo!'
indice = cadena.find('mundo')
print(f'Indice de la subcadena mundo: {indice}')

#Obtener el indice de la subcadema de Hola
#respeta mayusculas y minisculas de las variables strings

indice = cadena.find('hola')
#en este caso solo arrojaria un menos ya que "hola" en minusculas no existe
print(f'Indice de "hola" pero en minusculas: {indice}')

indice = cadena.find('Hola')
#caso en que "Hola" so existe
print(f'Indice la subcadena de Hola {indice}')