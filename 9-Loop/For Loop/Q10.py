Num = int(input("Enter a Number: "))

is_prime = True

if is_prime <= 0:
    is_prime = False

for i in range(2,Num):
    if Num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{Num} is a Prime Number.")
else:
    print(f"{Num} is not a prime number")
