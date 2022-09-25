class Calculadora:
    """
    Esto es una clase llamada Calculadora que nos sirve de ejemplo
    
    Atributos
    ---------
    num1:
        atributo uno de la clase
    num2:
        atributo dos de la clase
    
    Métodos
    -------
    sumar:
        Realiza la suma de 2 números
    restar:
        Realiza la resta de 2 números
    multiplicar:
        Realiza la multiplicación de 2 números
    dividir:
        Realiza la división del num2 entre el num1
        
    >>>>>>> sumar(4,2)
    """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        """Esta función realiza la suma
        """
        return self.num1+self.num2

    def restar(self):
        """Esta función realiza la resta
        """
        if(self.num2>self.num1):
            return self.num2-self.num1
        else:
            return self.num1-self.num2
    
    def multiplicar(self):
        """Esta función realiza la multiplicación
        """
        return self.num2*self.num1

    def dividir(self):
        """Esta función realiza la división
        """
        if(self.num2>self.num1):
            return self.num2/self.num1
        else:
            return self.num1/self.num2