Year = int(input("Enter any year to check its leap or not:"))

if(Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"{Year} is Leap Year")
else:
    print(f"{Year} is not Leap Year")