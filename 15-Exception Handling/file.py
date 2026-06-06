# x = int(input("Enter a Number: "))

# try:
#     print(10/x)
# # except ZeroDivisionError:
# except Exception as error:
#     print(f"Sorry you cannot divide by zero {error}")
# else:
#     print("There is no Error occur")
# finally:
#     print("I will run no metter no care of anything")

# print("This is valid for running")


age = int(input("Enter your age: "))
try:
    if age <= 10 or age>=19:
     raise ValueError("Enter the Age btw 10 to 19")
    else:
     print("Welcome to Club")
except Exception as error:
  print(f"The Error occur {error}")





print("The club will start soon")