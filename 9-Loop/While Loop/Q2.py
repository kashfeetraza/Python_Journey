Num = int(input("Enter a value: "))

while Num > 0:
    digit = Num % 10
    print(digit,end="")
    Num //= 10

