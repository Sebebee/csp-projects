
print("This low level calculator made by some guy who needs a good grade will kinda calculate your expenses.")
income= int (input("what is your monthly income?: "))
rent= int (input("how much do you spend on rent?: "))
utilities= int (input ("how much do you spend on utlities?: "))
Groceries= int (input("how much do you spend on Groceries: "))
transportation= int (input("how much do you spend on transportation: "))
savings = int (input("How much do you save a month?: "))

income = income-rent-utilities-Groceries-transportation
savings= savings/10
expenses = income/10

print("Your savings is %", savings)
print("Your monthly expenses is ", rent+utilities+Groceries+transportation)
