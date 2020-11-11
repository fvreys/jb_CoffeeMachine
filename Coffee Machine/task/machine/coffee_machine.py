class CoffeeMachine:
    # TO DO: 1/ Data structure for coffee content 2/ Simplify with it the method 'buy_coffee'

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water  # ml of water
        self.milk = milk  # ml of milk
        self.coffee_beans = coffee_beans  # g of coffee beans
        self.disposable_cups = disposable_cups
        self.money = money  # $

    def __str__(self):
        print_value = f"""
                    The coffee machine has:
                    {self.water} of water
                    {self.milk} of milk
                    {self.coffee_beans} of coffee beans
                    {self.disposable_cups} of disposable cups
                    ${self.money} of money"""
        return print_value


    def buy_coffee(self):
        type_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        if type_coffee == "1":
            if self.water < 250:
                print(f'Sorry, not enough water!')
            elif self.coffee_beans < 16:
                print(f'Sorry, not enough coffee beans!')
            else:
                print(f'I have enough resources, making you a coffee!')
                self.water -= 250
                self.coffee_beans -= 16
                self.disposable_cups -= 1
                self.money += 4
        elif type_coffee == "2":
            if self.water < 350:
                print(f'Sorry, not enough water!')
            elif self.milk < 75:
                print(f'Sorry, not enough milk!')
            elif self.coffee_beans < 20:
                print(f'Sorry, not enough coffee beans!')
            else:
                print(f'I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.disposable_cups -= 1
                self.money += 7
        elif type_coffee == "3":
            if self.water < 200:
                print(f'Sorry, not enough water!')
            elif self.milk < 100:
                print(f'Sorry, not enough milk!')
            elif self.coffee_beans < 12:
                print(f'Sorry, not enough coffee beans!')
            else:
                print(f'I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.disposable_cups -= 1
                self.money += 6
        elif type_coffee == "back":
            return

    def fill_supplies(self):
        filled_water: int = int(input('Write how many ml of water do you want to add: \n'))
        self.water += filled_water
        filled_milk: input = int(input('Write how many ml of milk do you want to add: \n'))
        self.milk += filled_milk
        filled_coffee_beans: int = int(input('Write how many grams of coffee beans do you want to add: \n'))
        self.coffee_beans += filled_coffee_beans
        filled_disposable_cups: int = int(input('Write how many disposable cups of coffee do you want to add: \n'))
        self.disposable_cups += filled_disposable_cups

    def take_money(self, money_now):
        print(f'I gave you ${money_now}')
        self.money = 0

    def take_action(self, action):
        if action != "exit":
            if action == "buy":
                self.buy_coffee()
            elif action == "fill":
                self.fill_supplies()
            elif action == "take":
                self.take_money(self.money)
            elif action == "remaining":
                print(self)


def main():
    # water = 400 ml of water, milk = 540 ml of milk, coffee_beans = 120 g of coffee beans, disposable_cups = 9,
    # money = 550  $
    coffee = CoffeeMachine(water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550)
    action = ""

    while action != "exit":
        action: str = input("Write action (buy, fill, take, remaining, exit): ")
        print()
        coffee.take_action(action)


main()
