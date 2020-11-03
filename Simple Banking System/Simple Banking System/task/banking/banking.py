# Write your code here
import random
import os.path
import sqlite3


class BankingSystem:
    def __init__(self):
        self.mii = "4"
        self.bin = self.mii + "00000"
        self.current_account = ''

        self.menu1 = ["1. Create an account",
                      "2. Log into account",
                      "0. Exit"]
        self.menu2 = ["1. Balance",
                      "2. Add income",
                      "3. Do transfer",
                      "4. Close account",
                      "5. Log out",
                      "0. Exit"]

    def start(self):

        if not os.path.isfile('card.s3db'):
            self.create_db()

        while True:
            self.show_menu(self.menu1)
            _input = input()
            if _input == '1':
                self.create_acc()
            if _input == '2':
                if self.validate():
                    if not self.log_in():
                        self.end_view()
                        break
            if _input == '0':
                self.end_view()
                break

    def create_acc(self):
        new_account_identifier = ''.join([str(random.randint(0, 9)) for _i in range(9)])
        new_card_number = self.bin + new_account_identifier + self.luhn(self.bin + new_account_identifier)
        new_pin = ''.join([str(random.randint(0, 9)) for _i in range(4)])
        self.add_card_db(new_card_number, new_pin)
        print(f"\nYour card has been created\n"
              f"Your card number:\n{new_card_number}\n"
              f"Your card PIN:\n{new_pin}\n")

    def log_in(self):
        while True:
            self.show_menu(self.menu2)
            _input = input()
            if _input == '1':
                print(f"\nBalance: {self.get_card_db(self.current_account)[3]}\n")
            if _input == '2':
                self.add_income()
            if _input == '3':
                self.do_transfer()
            if _input == '4':
                self.close_acc()
                self.current_account = ''
                return True
            if _input == '5':
                self.current_account = ''
                return True
            if _input == '0':
                self.current_account = ''
                return False

    def validate(self):
        card_nr = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")
        if self.val_card_db(card_nr, pin) is None:
            print("\nWrong card number or PIN!\n")
            return False
        else:
            self.current_account = card_nr
            print("\nYou have successfully logged in!\n")
            return True

    def add_income(self):
        amount = input("Enter income:\n")
        self.add_balance_db(self.current_account, amount)
        print("\nIncome was added!\n")

    def do_transfer(self):
        receiver = input("\nTransfer\nEnter card number:\n")
        if not self.luhn(receiver[:-1]) == receiver[-1]:
            print("\nProbably you made mistake in the card number. Please try again!\n")
            return
        if self.get_card_db(receiver) is None:
            print("\nSuch a card does not exist.\n")
            return
        amount = int(input("Enter how much money you want to transfer:\n"))
        if amount > self.get_card_db(self.current_account)[3]:
            print("\nNot enough money!\n")
            return
        self.rem_balance_db(self.current_account, amount)
        self.add_balance_db(receiver, amount)
        print("\nSuccess!\n")

    def close_acc(self):
        self.rem_card_db(self.current_account)
        print("\nThe account has been closed!\n")

    @staticmethod
    def create_db():
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ CREATE TABLE card(
                    id INTEGER PRIMARY KEY, 
                    number TEXT, 
                    pin TEXT, 
                    balance INTEGER DEFAULT 0
                );
            """)
        conn.commit()

    @staticmethod
    def add_card_db(number, pin):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ INSERT INTO card (number, pin)
                VALUES
                    (?, ?)
                ;
            """, (number, pin))
        conn.commit()

    @staticmethod
    def rem_card_db(number):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ DELETE FROM card 
                WHERE
                    number = ?
                ;
            """, (number,))
        conn.commit()

    @staticmethod
    def val_card_db(number, pin):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ SELECT *
                FROM
                    card
                WHERE
                    number = ?
                    AND pin = ? 
                ;
            """, (number, pin))
        return cur.fetchone()

    @staticmethod
    def get_card_db(number):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ SELECT *
                FROM
                    card
                WHERE
                    number = ?
                ;
            """, (number,))
        return cur.fetchone()

    @staticmethod
    def add_balance_db(number, amount):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ UPDATE card
                SET
                    balance = balance + ?
                WHERE
                    number = ? 
                ;
            """, (amount, number))
        conn.commit()

    @staticmethod
    def rem_balance_db(number, amount):
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ UPDATE card
                SET
                    balance = balance - ?
                WHERE
                    number = ? 
                ;
            """, (amount, number))
        conn.commit()

    @staticmethod
    def show_all_db():
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute(
            """ SELECT *
                FROM
                    card
                ;
            """)
        return cur.fetchall()

    @staticmethod
    def luhn(string):
        card_nr = [int(digit) for digit in string]
        odd_multi_2 = [card_nr[index] * 2 if index % 2 == 0 else card_nr[index] for index in range(len(card_nr))]
        control_number = sum([digit - 9 if digit > 9 else digit for digit in odd_multi_2])
        check_sum = 10 - control_number % 10
        return str(0 if check_sum == 10 else check_sum)

    @staticmethod
    def end_view():
        print("\nbye!")

    @staticmethod
    def show_menu(items):
        print('\n'.join(items))


banking_system = BankingSystem()
banking_system.start()

