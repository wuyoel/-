class Account:
	def __init__(self, balance):
		self.b = balance
		

	def deposit(self, money):
		self.b += money

	def withdraw(self, money):
		if self.b >= money:
			self.b -= money
			return True
		else:
			return False

	def __str__(self):
		return str(self.b)
	

while True:
    print("Please choose the operation you need:")
    choice = int(input("1. create account 2. deposit 3. withdraw 4. exit "))
    if choice == 1:
        m = int(input("Please specify your initial balance: "))
        a = Account(m)
        print("Now your balance is NT$", a.b)
    elif choice == 2:
        input_money = int(input("Please the amount of money you like to deposit: "))
        a.deposit(input_money)
        print("Now your balance is NT$", a.b)
    elif choice == 3:
        output_money = int(input("Please the amount of money you like to withdraw: "))
        if a.withdraw(output_money):
            print("Withdraw succesfully")
            print("Now your balance is NT$", a.b)
        else:
            print("Not enough money, Withdraw failed")
    else:
        print("Wrong operation, try again!")
	
	
