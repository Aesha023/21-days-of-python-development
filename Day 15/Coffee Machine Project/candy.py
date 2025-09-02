
MENU = {
    "Candy crush": {
        "ingredients": {
            "chocolate": 40,
            "milk": 20,
            "sugar": 60,
        },
        "cost": 150,
    },
    "Dairy milk": {
        "ingredients": {
            "chocolate": 30,
            "milk": 30,
            "sugar": 70,
        },
        "cost": 200,
    },
    "Kitkat": {
        "ingredients": {
            "chocolate": 60,
            "milk": 10,
            "sugar": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "chocolate": 700,
    "milk": 500,
    "sugar": 500,
}



def is_sufficient_ingredients(amount_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in amount_ingredients:
        if amount_ingredients[item] >= resources[item]
            print(f"sorry not enough resources {item}.")
            return False
        return True




is_on = True

while is_on:
    choice = input("Which candy would you like to have?").lower()
    if choice == "off":
        is_on = False

