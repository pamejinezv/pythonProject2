import random

def funcionValida(valor1, valor2, valor3 ):
    print('Escribe tu opcion en minusculas, piedra, papel o tijera')
    cadenaUser = input()
    print(f'ELEGISTE: {cadenaUser}')
    opciones = ['piedra', 'papel', 'tijera']
    cadenaPC = random.choice(opciones)
    print(f'LA PC ELIGIO: {cadenaPC}')

    if cadenaUser == valor1 and cadenaPC == valor2:
        print('PERDISTE!')
    elif cadenaUser == valor1 and cadenaPC == valor3:
        print('GANASTE!')
    elif cadenaUser == cadenaPC:
        print('EMPATE!')
    elif cadenaUser == valor2 and cadenaPC == valor3:
        print('PERDISTE!')
    elif cadenaUser == valor2 and cadenaPC == valor1:
        print('GANASTE!')
    elif cadenaUser == valor3 and cadenaPC == valor1:
        print('PERDISTE!')
    elif cadenaUser == valor3 and cadenaPC == valor2:
        print('GANASTE!')
    else:
        print('Opcion no valida, elige una valida')
    return


#if __name__ == '__main__':

  #funcionValida(valor1 ='piedra' , valor2 = 'papel', valor3 = 'tijera')
