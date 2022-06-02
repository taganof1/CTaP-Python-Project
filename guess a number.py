import random

numbergen=random.randint(1,10)

usernumber=int(input("Guess A Number Between 1 to 10\n: "))
if usernumber==numbergen:
    print("Correct!")
else:
     print("Incorrect!")1