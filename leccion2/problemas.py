from datetime import datetime
from dateutil.relativedelta import relativedelta


def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
def calcularEdad(fecha_nac):
    fecha_nacimiento = datetime.strptime(fecha_nac, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), fecha_nacimiento)
    return edad.years

def suma(a, b):
    return a+b

def potencia(a,b):
    return a**b

def saludar(nombre):
    return f"Buenos días, {nombre}"