time = int (input("what time is it?(24 hour format): "))

if time >= 2000 and time<=2359:
    print("good evening!!")
elif time <2000 and time>1200:
    print("Good Afternoon!")
elif time<=1200 and time>800:
    print("Good morning")
else:
    print("That may be an invalid format, try military time.")