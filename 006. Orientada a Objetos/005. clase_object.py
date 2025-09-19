#clase_object
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#Sobreescribir el metodo __str__
    def __str__(self): #regresa una cadena
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}''' #super ayuda acceder el comportamiento que esta oculto de las clases 

#Codido principal
persona1 = Persona('Luis', 'Isaac')
print(persona1) # el metodo __str__ se llama dsde print
#tambien funciona asi
print(persona1.__str__())


