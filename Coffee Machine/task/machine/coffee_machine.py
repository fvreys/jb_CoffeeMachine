class CoffeeMachine:

    def __init__(self):
        # Supplies at start
        self.water = 400  # ml of water
        self.milk = 540  # ml of milk
        self.coffee_beans = 120  # g of coffee beans
        self.disposable_cups = 9
        self.money = 550  # $

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

    def display_supplies(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'${self.money} of money')

    def take_action(self, action):
        if action != "exit":
            if action == "buy":
                self.buy_coffee()
            elif action == "fill":
                self.fill_supplies()
            elif action == "take":
                self.take_money(self.money)
            elif action == "remaining":
                self.display_supplies()


def main():
    coffee = CoffeeMachine()
    action = ""

    while action != "exit":
        action: str = input("Write action (buy, fill, take, remaining, exit): ")
        print()
        coffee.take_action(action)


main()
