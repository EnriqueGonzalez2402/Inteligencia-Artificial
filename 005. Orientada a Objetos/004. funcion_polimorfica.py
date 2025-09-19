#funcion_polimorfica

#polimorfismo se puede definir como el comportamiento de multiples maneras dependiendo del tipo de dato y si existe es alguin tipo de sobreescritura
class Animal:
    def hacer_sonido(selff):
        print('Hago pitido')


class Perro(Animal):
    def hacer_sonido(selff):
        print('Puedo ladrar')


class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# funcion polimorfica
def hacer_sonido_animal(animal):
        animal.hacer_sonido()

print('*** Ejemplo de Polimorfismo ***')

print('Clase Padre Animal: ')

animal1 = Animal()
hacer_sonido_animal(animal1)
#Definimos objetos en clase hija Perro
print('\nClase Hija Perro')
perro1 = Perro()
hacer_sonido_animal(perro1)

#Definimos objetos en clase hija Gato
print('\nClase Hija Gato')   
gato1 = Gato()
hacer_sonido_animal(gato1)