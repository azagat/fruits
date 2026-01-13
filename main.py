fruits = ("apple", "banana", "oranges", "dragon fruit")

for fruit in fruits:
    print(fruit)
    

userFruit = input("What is your favorite fruit? ")

if userFruit in fruits:
    print("Nice, mine too!")
else:
    print("Not my favorite, but good choice!")