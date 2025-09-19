#ejercicio_empleados

print ('*** Sistma de Empleados ***')
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_depertamento = input('Es jefe departamento (Si/No)? ')

# Vamos a convertir a un tipo bool la variable de es_jefe
es_jefe_depertamento = es_jefe_depertamento.lower() == 'si'

#Imprimir los valores
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es jefe de Departamento? {es_jefe_depertamento}')