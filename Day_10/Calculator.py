import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = 0
print(art.logo)
while True:
    if first_number == 0:
        first_number = int(input('Type a number: '))
    operation = input('Select opertaion "+", "-", "*" or "/": ')
    second_number = int(input('Type second number: '))
    result = operations[operation](first_number,second_number)
    print(f'El resultado es: {result}')
    continua = input(f'Want to continue workin with {result}? (y/n): ')
    if continua == 'n':
        first_number = 0
    else:
        first_number = result
        print(f'first number: {first_number}')