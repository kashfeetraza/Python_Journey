Num = int(input("Enter a Value : "))

for i in range(1,Num+1):
    if Num % i == 0:
        print(f"The factor of {Num} is {i}")