Num = int(input("Enter a value: "))
orginal_Num = Num
reversed_Num = 0

while Num > 0:
    digit = Num % 10
    reversed_Num = (reversed_Num * 10) + digit
    Num //= 10

print("Reverse Number: ",reversed_Num)

if reversed_Num == orginal_Num:
    print(f"The Number is pallindromic Number")
else:
    print(f"The Number is not pallindromic Number")