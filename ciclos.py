continuar = True
contador = 0
while continuar:
    contador = contador + 1
    print(f'{contador}')
    print('Deseas continuar:')
    respuesta = input()

    if respuesta == 's':
        continue
    else:
        continuar = False

for i in range(10):
    print(f'Numero:{i+1}')

    if i == 4:
        break

print('FIN')