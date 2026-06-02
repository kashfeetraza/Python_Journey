Num = int(input("Enter a Value : "))
Sum_of_factor = 0

for i in range(1,Num):
    if Num % i == 0:
        Sum_of_factor += i
        
if Sum_of_factor == Num:
    print("This Number is prime Number")
else:
    print("The Number is Not Prime")
   
