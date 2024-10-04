def enlightenMe(type):
  insert = input(f"what is your monthly {type}: ")
  return int(insert)



print("This low level calculator made by some guy who needs a good grade and will kinda calculate your expenses.")
inIncome= enlightenMe("income")
rent= enlightenMe("rent")
utilities= enlightenMe("utilites")
Groceries= enlightenMe("groceries")
transportation= enlightenMe("transportation")
percentageSavings = enlightenMe("what percentage of your income do you wanna save?")

def calculate(type,amount):
 per = amount/inIncome * 100
 print(f"your {type} is {per}% of your income. ")

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
 
calculate("rent",rent)