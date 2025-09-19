#sobreescritura

class Animal: 
    def comer(self):
        print('Como muchas veces al día')
    
    def dormir(self):
        print('Duermo muchas horas')


#clase hija (se pone nomnre de clase padre) flecha arriba indica de donde estamos heredando
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    #Sobreescritura del metodo dormir
    def dormir(self):
        print ('Duermo 15 horas al día') #"definimos comportamiento"

#Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() #Se llama el metodo sobreescrito de la clase hija
perro1.hacer_sonido()