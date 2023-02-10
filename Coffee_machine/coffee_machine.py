MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_print(resoures_dict):
    """남은 재료의 양 출력"""
    print(f"Water: {resoures_dict['water']}ml")
    print(f"Milk: {resoures_dict['milk']}ml")
    print(f"Coffee: {resoures_dict['coffee']}g")


def is_resources_enough(drink_dict, resources_dict):
    """음료와 남은 재료 비교 후 제조 가능 여부 반환"""
    for Any in drink_dict:
        if drink_dict[Any] > resources_dict[Any]:
            print(f"Sorry there is not enough {Any}.")
            return False
        else:
            return True


def coin_process():
    """음료의 가격을 제대로 지불 했는지와 비용 반환"""
    print("Please insert coin.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total


def profit_and_changes(user_pay, cost):
    """거스름 돈 출력과 수익금 반환"""
    drink_cost = cost
    change = round(user_pay - drink_cost, 3)
    if change >= 0:
        print(f"Here is ${change} in change.")
        return drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def drink_out(drink_dict, resources_dict):
    """사용한 재료 계산"""
    for Any in drink_dict['ingredients']:
        resources_dict[Any] -= drink_dict['ingredients'][Any]


def machine():
    global MENU
    machine_on = True
    money = 0

    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == 'off':
            machine_on = False
        elif user_input == 'report':
            resources_print(resources)
            print(f"Money: ${money}")
        elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            choice = MENU[user_input]
            if is_resources_enough(choice['ingredients'], resources):
                payment = coin_process()
                profit = profit_and_changes(payment, choice['cost'])
                if profit != 0:
                    drink_out(choice, resources)
                    money += profit
                    print(f"Here is your {user_input} ☕. Enjoy!")


machine()