import re


correo = 'pame.jinezv@gmail.com.mx'
patron = '^[(a-zA-Z0-9\_\-\.)]+@[(a-zA-Z\_\-\.)]+\.[(a-zA-Z)]{2,}$'
valida = re.match(patron, correo)

if valida:
   print('El correo electronico Correcto')
else:
    print('Correo electronico Incorrecto')


numeroTelefonico = '(188)1456719'
patronN= '^\(([1-9]{3,})\)[0-9]{7}$'
# [PV] poner entre llaves {9,} indica que pueden ser 9 o mas caracteres deberia ser {9}
patronSP = '^[1-9]{1}[0-9]{9,}$'

validaNCP = re.match(patronN, numeroTelefonico)
validaSP = re.match(patronSP, numeroTelefonico)
if validaNCP or validaSP:
   print('El numero telefonico Correcto')
else:
    print('El numero telefonico Incorrecto')


curp = 'JIVP910813MGTNLM05'
patronC = '^[a-zA-Z]{4}[0-9]{6}[HM]{1}[a-zA-Z]{5}[0-9]{2}$'
validarCurp = re.match(patronC, curp)

if validarCurp:
    print('La CURP es Correcta')
else:
    print('La CURP es Incorrecta')


rfc = 'JIVP910813797'
patronR = '^[a-zA-Z]{4}[0-9]{6}[0-9]{3}$'
validarRfc = re.match(patronR, rfc)

if validarRfc:
    print('El RFC es Correcto')
else:
    print('El RFC es Incorrecto')

