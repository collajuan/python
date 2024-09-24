def calculadora (operacion: callable, n1, n2):
    resultado = operacion(n1,n2)
    return resultado

suma = lambda n1, n2: n1 + n2
resta = lambda n1, n2: n1 - n2
multiplicacion = lambda n1, n2: n1 * n2
division = lambda n1, n2: n1 / n2

print(calculadora(suma,2,3))   