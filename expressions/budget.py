def enlightenMe(type):
  enter = input(f"what is your monthly {type}: ")
  return int(enter)



print("This low level calculator made by some guy who needs a good grade and will kinda calculate your expenses.")
inIncome= enlightenMe("income")
rent= enlightenMe("rent")
utilities= enlightenMe("utilites")
Groceries= enlightenMe("groceries")
transportation= enlightenMe("transportation")


def calculate(type,amount):
 per = amount/inIncome * 100
 print(f"your {type} is {per}% of your income. ")

expenses = inIncome-rent-utilities-Groceries-transportation
savings= inIncome*.2
spending = inIncome-expenses

print("Your monthly savings is ",savings)
print("Your monthly expenses is ", expenses)
print("Your spending money is",spending)
 
calculate("rent",rent)
calculate("utilities",utilities)
calculate("groceries",Groceries)
calculate("transportation",transportation)
#put it on the beat bro