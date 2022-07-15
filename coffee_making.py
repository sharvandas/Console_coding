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

e = MENU["espresso"]["cost"]
c = MENU["cappuccino"]["cost"]
l = MENU["latte"]["cost"]
machine_on = True

# global e_m
# e_m = 0




# off
def off():
    print("Closing at: ")
    report()
    print("Machine is under maintainence!")

#report
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}") #\nMoney: ${e_m}

def collect_money(user_input):

    print("Please insert coins")
    quarters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    penny = int(input("How many penny?: "))
    t_m = round((0.5 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * penny),2)
    print(f"Collected money ${t_m}")


    if user_input == 'latte':
        print(f"cost for {user_input} is: {l}")
        if t_m > l:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            change = t_m - l
            change = round(change, 2)
            #e_m += l
            print(f"Please collect your change:{change}")
            print(f"Here id your {user_input}. Enjoy")
        else:
            print("Insufficient Amount")
    elif user_input == "espresso":
        print(f"cost for {user_input} is: ${e}")
        if t_m > e:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            change = t_m - e
            change = round(change, 2)
            #e_m += e
            print(f"Please collect your change: ${change}")
            print(f"Here id your {user_input}. Enjoy")
        else:
            print("Insufficient Amount")
    elif user_input == "cappuccino":
        print(f"cost for {user_input} is: {c}")
        if t_m > c:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            change = t_m - c
            change = round(change,2)
            #e_m += c
            print(f"Please collect your change: ${change}")
            print(f"Here id your {user_input}. Enjoy")
        else:
            print("Insufficient Amount")

def check_availability(user_input):
    r_w = resources["water"]
    r_m = resources["milk"]
    r_c = resources["coffee"]
    if user_input == "cappuccino":
        if r_w >= MENU["cappuccino"]["ingredients"]["water"] and r_m >= MENU["cappuccino"]["ingredients"]["milk"] and r_c >= MENU["cappuccino"]["ingredients"]["coffee"]:
            collect_money(user_choice)
        else:
            print("Sorry there is not enough material.")
    if user_input == "latte":
        if r_w >= MENU["latte"]["ingredients"]["water"] and r_m >= MENU["latte"]["ingredients"]["milk"] and r_c >= MENU["latte"]["ingredients"]["coffee"]:
            collect_money(user_choice)
        else:
            print("Sorry there is not enough material.")
    if user_input == "espresso":
        if r_w >= MENU["espresso"]["ingredients"]["water"] and r_c >= MENU["espresso"]["ingredients"]["coffee"]:
            collect_money(user_choice)
        else:
            print("Sorry there is not enough material.")






print("-----------------------------------------")
while machine_on:
    user_choice = input("What would you like? (espresso / latte / cappuccino):").lower()
    print(user_choice)
    if user_choice == "off":
        machine_on = False
        off()
    elif user_choice == "report":
        report()
    elif (user_choice):
        check_availability(user_choice)

    print("Visit Again")





