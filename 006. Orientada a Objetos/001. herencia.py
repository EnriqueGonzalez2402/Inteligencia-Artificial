#herencia

class Animal: 
    def comer(self):
        print('Como muchas veces al día')
    
    def dormir(self):
        print('Duermo muchas horas')


#clase hija (se pone nomnre de clase padre) flecha arriba indica de donde estamos heredando
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

#Programa principla
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()