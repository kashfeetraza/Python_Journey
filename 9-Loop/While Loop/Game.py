import random

Random_value = random.randint(1,10)

# print(Random_value)

tries = 0

while True:
    Guess_Num = int(input("Enter a Num to Guess: "))

    if Random_value == Guess_Num:
     tries += 1
     print(f"you are right with the tries {tries}")
     break

    elif Guess_Num < Random_value:
      print("the random value is little higher")
      tries += 1

    elif Guess_Num > Random_value:
      print("The random value is little lower")
      tries += 1

    else:
     tries += 1
     print("Your Guess is Wrong")

