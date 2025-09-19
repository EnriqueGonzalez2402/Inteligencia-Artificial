#polimorfismo se puede definir como el comportamiento de multiples maneras dependiendo del tipo de dato y si existe es alguin tipo de sobreescritura
class Animal:
    def hacer_sonido(selff):
        print('Hago pitido')


class Perro(Animal):
    pass # si solo queremos defirnir solo la funcion solo agregamos si no queremos definir algo
    #def hacer_sonido(self):
        #print('Puedo ladrar')


class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')


print('*** Ejemplo de Polimorfismo ***')

print('Clase Padre Animal: ')

animal1 = Animal()
animal1.hacer_sonido()

#Definimos objetos en clase hija Perro
print('\nClase Hija Perro')
perro1 = Perro()
perro1.hacer_sonido() #Polimorfismo

#Definimos objetos en clase hija Gato
print('\nClase Hija Gato')   
gato1 = Gato()
gato1.hacer_sonido()