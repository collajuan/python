

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
    arn = adn.translate(mydict)
    # arn = arn_medio.replace('T','U')
    print(arn)

adn='ACGTTGGTAAGG'
adn_to_arn(adn)