class CoffeeMachine:
    def __init__(self, resources):
        self.resources = resources
        self.espresso = Beverage(250, 0, 16, 1, 4)
        self.latte = Beverage(350, 75, 20, 1, 7)
        self.cappuccino = Beverage(200, 100, 12, 1, 6)

        self.state = ""

    def buy(self, string):
        if self.state == "buy":
            if string == "1":
                self.espresso.make_beverage(self.resources)
            if string == "2":
                self.latte.make_beverage(self.resources)
            if string == "3":
                self.cappuccino.make_beverage(self.resources)

            self.action_message()
            return

        if string == "buy":
            self.state = "buy"
            print("What do you want to buy? "
                  "1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            return

    def fill(self, string):
        if string == "fill":
            self.state = "fill"
            print("Write how many ml of water do you want to add:")
            self.resources.state = "water"
            return
        if self.resources.state == "water":
            self.resources.add_resources(int(string))
            print("Write how many ml of milk do you want to add:")
            self.resources.state = "milk"
            return
        if self.resources.state == "milk":
            self.resources.add_resources(int(string))
            print("Write how many grams of coffee beans do you want to add:")
            self.resources.state = "beans"
            return
        if self.resources.state == "beans":
            self.resources.add_resources(int(string))
            print("Write how many disposable cups of coffee do you want to add:")
            self.resources.state = "cups"
            return
        if self.resources.state == "cups":
            self.resources.add_resources(int(string))

        self.resources.state = ""
        self.action_message()
        return

    def remaining(self):
        print("The coffee machine has:")
        print(self.resources)
        self.action_message()

    def take(self):
        print(f"I gave you ${self.resources.money}")
        self.resources.withdraw_all_money()
        self.action_message()

    def action_message(self):
        self.state = ""
        print()
        print("Write action (buy, fill, take, remaining, exit):")

    def user_input(self, string):
        if string == "buy" or self.state == "buy":
            self.buy(string)
        if string == "fill" or self.state == "fill":
            self.fill(string)
        if string == "exit":
            self.state = "exit"
        if string == "remaining":
            self.remaining()
        if string == "take":
            self.take()


class Resources:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

        self.state = ""

    def __repr__(self):
        return f"{self.water} of water \n" \
               f"{self.milk} of milk \n" \
               f"{self.beans} of coffee beans \n" \
               f"{self.cups} of disposable cups \n" \
               f"${self.money} of money"

    def add_resources(self, amount):
        if self.state == "water":
            self.water += amount
        if self.state == "milk":
            self.milk += amount
        if self.state == "beans":
            self.beans += amount
        if self.state == "cups":
            self.cups += amount

    def update_resources(self, water, milk, beans, cups, money):
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money

    def withdraw_all_money(self):
        self.money = 0


class Beverage:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def make_beverage(self, resources):
        if self.water > resources.water:
            print("Sorry, not enough water!")
            return
        if self.milk > resources.milk:
            print("Sorry, not enough milk!")
            return
        if self.beans > resources.beans:
            print("Sorry, not enough beans!")
            return
        if self.cups > resources.cups:
            print("Sorry, not enough cups!")
            return

        print("I have enough resources, making you a coffee!")
        resources.update_resources(self.water, self.milk, self.beans, self.cups, self.money)
        return


machine = CoffeeMachine(Resources(400, 540, 120, 9, 550))
machine.action_message()
while machine.state != "exit":
    machine.user_input(input())
