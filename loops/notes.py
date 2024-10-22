import random
wordBank=["womp","hawktuah","hello","sigma"]
word ="placeholder"
rand = random.randint(1,4)

if rand == 1:
    word = "womp"
elif rand ==2:
    word = "hawktuah"
elif rand ==3:
    word = "hello"
elif rand ==4:
    word = "sigma"

print(word)