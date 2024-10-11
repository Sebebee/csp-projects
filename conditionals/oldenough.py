age = int (input("what is your age?: "))

if age >= 18:
    print("you are old enough to vote")
elif age <18 and age>15:
    print("You are old enough to drive")
elif age<16 and age==15:
    print("You are old enough to get a drivers permit")
elif age<15 and age>=5:
    print("You are old enough to go to school")   
else:
    print("you too young cuz")