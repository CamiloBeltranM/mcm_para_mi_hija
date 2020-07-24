numero_1 = int(input(f'Ingresa el primer numero: '))
numero_2 = int(input(f'Ingresa el segundo numero: '))
limite = int(input(f'Hasta que numero multiplicamos: '))
contador_externo = 1
contador_interno = 1
contador = 0

while contador_externo <=limite:
    while contador_interno <= limite:
        if contador_interno * numero_2 == contador_externo * numero_1:
            contador += 1
            break
        print((contador_externo * numero_1), (contador_interno * numero_2)+ numero_2)
        print(contador_externo, contador_interno + 2)
        contador_interno += 1
    if contador != 0:
        break
    contador_externo += 1
    contador_interno = 0
print('')
    

        

