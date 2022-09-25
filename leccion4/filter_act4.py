def esPrimo(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

numeros = [3,4,8,5,5,22,13]
primos = list(filter(esPrimo, numeros))

print(primos)

lam = lambda num : all([num % i for i in range(2, num)])
aux_primos = list(filter(lam, numeros))
        
print(aux_primos)