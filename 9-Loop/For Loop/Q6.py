Num = int(input("Enter a value : "))
fatorial = 1

for i in range(1,Num+1):
    fatorial *= i

print(f"The Factorial of {Num} is {fatorial}")