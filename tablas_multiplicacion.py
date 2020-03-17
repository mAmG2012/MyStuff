# Imprime tablas de multiplicacion hasta donde indiquemos en las variables
# Largo y Hasta


# Datos en eje X:
Largo = 12
# Datos en eje Y:
Hasta = 12

def imprimeMultiplos(n):
    i = 1
    while i <= Largo:
        print(n*i, end='\t')
        i += 1
    print('')

def imprimeTablamult(mayor):
    h = 1
    while h <= mayor:
        imprimeMultiplos(h)
        h += 1

print(' ---> Tablas de Multiplicar del 1 al '  + str(Hasta) + ' <----')
imprimeTablamult(Hasta)