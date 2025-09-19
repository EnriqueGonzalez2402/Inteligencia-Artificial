#ejercicio_creacion_de_gmail
print('*** Generador de Email ***\n')

nombre_usuario = ' Luis Enrique GonZaleZ Isaac '
print(f'Nombre de usuario: {nombre_usuario}')
nombre_sin_espacios = nombre_usuario.strip()
nombre_minusculas = nombre_sin_espacios.lower()
nombre_normaliZadou = nombre_minusculas.replace(' ', '.')
print(f'Nombre normaliZado: {nombre_normaliZadou}')
print('\n')

nombre_empresa = ' Global Mentoring '
print(f'Nombre empresa: {nombre_empresa}')
nombre_sin_espacios = nombre_empresa.strip()
nombre_minusculas = nombre_sin_espacios.lower()
nombre_normaliZado = nombre_minusculas.replace(' ', '')
extension = '.com.mx'
arroba = '@'
print(f'Extensión del dominio: {extension}')
nombre_dominio_completo = ''.join([arroba,nombre_normaliZado,extension])
print(f'Dominio de email normaliZado : {nombre_dominio_completo}')
print('\n')
final = nombre_normaliZadou+nombre_dominio_completo
print(f'Email final generado: {final}')