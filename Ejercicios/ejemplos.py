

# string = input('ponga string: ')
# if len(string) > 0:
#     if string[0].lower() == string[-1].lower():
#         print('son iguales')
#     else:
#         print('no lo son')


# string = input('numero ')
# string_inv = string[::-1]
# print(string_inv)

# print('es palindromo') if string == string_inv else print('no es plaindromo')

# TODO hacer pequeña base de datos
# base_de_datos = {
#     1: {
#         'nombre': 'juan',
#         'edad' : 34,
#         'notas': [1,2,3]
#         },
#     2: {
#         'nombre': 'juan',
#         'edad' : 34,
#         'notas': [1,2,3]}
#     }


# print(base_de_datos[2]['nombre'])

# TODO validar lista de telefonos nuve digitos y empezar por 6 o 7
telefonos=['696 02 68 63', '666 66 66  66','74782 19_32']
def validar_telefono(telefono):
    for telefono in telefonos:
        telefono = telefono.replace(" ","")
        if len(telefono) == 9 and telefono[0] in ('6','7'):
                print(telefono, 'telefono ok')
        else:
            print(telefono, 'no valido')

# validar_telefono(telefonos)
# TODO validar un diccionario con emails y si estan activos o no
emails = {
    "joaquin":{
        "email": "starseeker_noether@outlook.com",
        "activated": True
    },
    "rosalinda":{
        "email": "example@gmail.com",
        "activated": False
    },
}

def validar_email(email):
    emails_ok=[]
    for usr in email:
        #  print(email[usr]['activated'])
         if email[usr]['activated'] == True:
              emails_ok.append(email[usr]['email'])
    return emails_ok


# print(validar_email(emails))

# TODO invertir lista
def invertir(lista: list|tuple) -> list|tuple:
     return lista[::-1]

lista = [1,2,3,4,5]
# print(invertir(lista))


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
