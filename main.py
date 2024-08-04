manu = {
    "doodhpatti" :{
        "ingredients":{
            "milk":100,
            "tea": 24,
        },
        "cost": 50,
    },
    "kashmirichai":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "tea":24,
        },
        "cost": 60,
    },


    "kehwa":{
        "ingredients":{
            "water":50,
            "tea":18,
        },
        "cost":40,
    }

}

profits = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "tea" : 100,
}

def is_resoucrc_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_Money():
    print("Please insert Money")
    total = int(input())
    return total

def is_transaction_successful(money_received , drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is RS:{change} in change.")
        global profits
        profits += drink_cost
        return True
    else:
        print("Sorry that's not enough money .Money refunded.")
        return False

def make_chai(drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (doodh Patti / Kashmiri Chai / Kehwa)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"tea: {resources['tea']}g")
        print(f"Money: RS:{profits}")
    else:
        drink = manu[choice]
        if is_resoucrc_sufficient(drink["ingredients"]):
            payment = process_Money()
            if is_transaction_successful(payment , drink["cost"]):
                make_chai(choice , drink["ingredients"])
