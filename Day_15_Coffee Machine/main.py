MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    'money': 0
}

def report():
    print(f'Water: {resources['water']}ml')
    print(f'Milk: {resources['milk']}ml')
    print(f'Coffe: {resources['coffee']}g')
    print(f'Money: ${resources['money']}')

def check_resources(machine, drink):
    """Return 1 if there is enough resources"""
    for key in drink['ingredients']:
        if machine[key] < drink['ingredients'][key]:
            return f'Sorry there is not enough {key}.'
    return 1    

def process_coins(drink_cost):
    """Retorna -1 si no hay sufuciente dinero y 1 si es suficiente y/o hay cambio"""
    quarters = float(input('How many quarters?: ')) * 0.25
    dimes = float(input('How many dimes?: ')) * 0.1
    nickels = float(input('How many nickel?: ')) * 0.05
    pennies = float(input('How many pennies?: ')) * 0.01
    coins = quarters + dimes + nickels + pennies
    if drink_cost > coins:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    elif drink_cost < coins:
        print(f"Here is ${round(coins - drink_cost, 2)} dollars in change")
        return 1
    else:
        return 1

def update_resources(machine, product):
    for key in machine:
        if key == 'money':
            machine[key] = machine[key] + product['cost']
        else:    
            machine[key] = machine[key] - product['ingredients'][key]
    return machine

machine_on = True

while machine_on:
    answer = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if answer == 'report':
        report()
    elif answer == 'off':
        machine_on = False
    else:
        enough_resources = check_resources(resources, MENU[answer])
        if enough_resources != 1:
            print(enough_resources)
        else:
            if process_coins(MENU[answer]["cost"]) != -1:
                resources = update_resources(resources, MENU[answer])
                print(f'Here is your {answer}. Enjoy!')