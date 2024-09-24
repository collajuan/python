#TODO Pedir numero hasta recibir 0 y devolver la suma de todos esos numeros
def sumar_input() -> int|float:
    suma = 0
    numero = 1

    while numero !=0:
          numero = int(input('ingrese un numero: '))
          suma += numero

    return suma

# resultado = sumar_input()
# print('La suma es: ', resultado)

#TODO convertir ADN a ARN
def adn_to_arn(adn: str) -> str:
    mydict = {ord('A'): 'U', ord('T'):'A', ord('C'):'G', ord('G'):'C'}
    arn = adn.upper().translate(mydict)
    # arn = arn_medio.replace('T','U')
    print(arn)

adn='ACGTTGGTAAgg'
# adn_to_arn(adn)

#TODO recibe un string y devuelve lista con el cuadrado de los numeros que encuentre
def numeros_al_cuadrado(string: str) -> list:
    lista_cuadrados = []
    lista_string = list(string)
    print(lista_string)
    # print(type(lista_string))
    for n in lista_string:
         if n.isdigit():
              lista_cuadrados.append(int(n)**2)
    return lista_cuadrados        

# print(numeros_al_cuadrado('sdfsdf5fdg897'))

#TODO validar IP
# from ipaddress import ip_address

def validar_ip(ip: str) -> bool:
    #! ip_address(input('indique una IP: ')))  aun no vimos try - except
    numeros_ip=ip.split('.')
    print(numeros_ip)
    for numero in numeros_ip:
        if (not 0<= int(numero) <= 255):
            return 'IP no valida'
    return 'IP valdia'

# print(validar_ip('192.1680.1.1'))

#TODO 4 numeros narcisistas con 3 cifras 1**3 + 5**3 + 3**3 = 153
def numero_narcisista
(num):

