def enlightenMe(type):
   
   return 0 



print("This low level calculator made by some guy who needs a good grade will kinda calculate your expenses.")
inIncome= int (input("what is your monthly income?: "))
rent= int (input("how much do you spend on rent?: "))
utilities= int (input ("how much do you spend on utlities?: "))
Groceries= int (input("how much do you spend on Groceries: "))
transportation= int (input("how much do you spend on transportation: "))
percentageSavings = int (input("what percentage of your income would you like to save?: "))

rentP= rent/inIncome
utilitiesP= utilities/inIncome
Groceriesp=Groceries/inIncome
transportationP=transportation/inIncome

expenses = inIncome-rent-utilities-Groceries-transportation
savings= inIncome/percentageSavings
spending = inIncome-expenses

print("Your monthly savings is ",savings*100)
print("Your monthly expenses is ", expenses)
print("Your spending money is",spending)
 
print("your rent is%",rentP*100,"of your income")
print("your utilities is%",utilitiesP*100,"of your income")
print("your Groceries is%",Groceriesp*100,"of your income")
print("your transportation is%",transportationP*100,"of your income")