class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be positive.')
        elif amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount




class ATMController:
    def __init__(self):
        self.atm = ATM()

    def get_number(self, prompt):
        while True:
            number = input(prompt)
            if number.replace('.', '', 1).isdigit():
                return float(number)
            print('Please enter a valid number.')

    def display_menu(self):
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance}')

    def deposit(self):
        amount = self.get_number('Enter the amount to deposit: ')
        self.atm.deposit(amount)
        print(f'Successfully deposited ${amount}.')

    def withdraw(self):
        amount = self.get_number('Enter the amount to withdraw: ')
        self.atm.withdraw(amount)
        print(f'Successfully withdrew ${amount}.')

    def run(self):
        while True:
            self.display_menu()
            choice = input('Please choose an option: ')
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Thank you for using the ATM.')
                break
            else:
                print('Invalid choice. Please try again.')





def main():
    atm_controller = ATMController()
    atm_controller.run()

if __name__ == '__main__':
    main()
