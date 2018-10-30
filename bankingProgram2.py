#Katie Williamson
#Assignment 8.1
#Thank you for allowing us more time to truely understand how to use classes.

#look at bankingProgram.py for any errors or to understand the code better
from bankingProgram import BankAccount, CheckingAccount, SavingsAccount

while True:
	try:
		act1 = int(input('Do you want to open an account?\nPress "1" for Yes\nPress "2" for No\n'))
		#If user wants to open an account
		if act1 == 1:
			act2 = int(input('Do you want to open a Savings Account or Checking Account?\nPress "1" for Savings\nPress "2" for Checking\n'))
			#If user want to create a Savings Account
			if act2 == 1:
				print("Minimum Balance is $50.00. \nMonthly Interest is 2%.\n")
				accountNumber = int(input('What do you want your account number to be: '))
				balance = float(input('What is your Balance: '))
				#Passing values to attributes in SavingsAccount
				savingsAccount = SavingsAccount(accountNumber, balance, 2)
				savingsAccount.addInterest()
				act3 = 1
				#Continue asking unless the user wants to quit
				while act3 != 4:
					act3 = int(input('What would you like to do?\nPress "1" to make a deposit\nPress "2" to make a withdrawal\nPress "3" to check your balance\nPress "4" to exit\n'))
					#If user wants to deposit money
					if act3 == 1:
						savingsAccount.deposit()
						#I didn't know how often I should use addInterest() so I just added it here knowing that everytime they make a deposit they will get interest. I just wanted to show it can work in multiple places.
						savingsAccount.addInterest()
					#If user wants to withdraw money
					if act3 == 2:
						savingsAccount.withDrawal()
					#If user wants to check their balance
					if act3 == 3:
						savingsAccount.getBalance()
					#If user wants to quit
					if act3 == 4:
						print('\nHave a nice Day!')
						break
			#If user wants to create a Checking Account
			if act2 == 2:
				#User input
				checkingAccountNumber = int(input('What do you want your account number to be: '))
				checkingAccountBalance = float(input('What is your Balance: '))
				#Passing values to attributes in CheckingAccount
				checkingAccount = CheckingAccount(checkingAccountNumber, checkingAccountBalance, 5.0, 50.00)
				checkingAccount.checkMinimumBalance()
				act3 = 1
				while act3 != 4:
					act3 = int(input('What would you like to do?\nPress "1" to make a deposit\nPress "2" to make a withdrawal\nPress "3" to check your balance\nPress "4" to exit\n'))
					#If user wants to deposit money
					if act3 == 1:
						checkingAccount.deposit()
						checkingAccount.checkMinimumBalance()
					#If user wants to withdraw money
					if act3 == 2:
						checkingAccount.withDrawal()
						checkingAccount.checkMinimumBalance()
					#If user wants to check their balance
					if act3 == 3:
						checkingAccount.getBalance()
					#If user wants to quit
					if act3 == 4:
						print('\nHave a nice Day!')
						break
		#If user doesn't want to open an account
		if act1 == 2:
			print('\nHave a Nice Day!')
			break
	except:
		print('You broke it!\n')

