Num = int(input("Enter a value : "))

even_count = 0
odd_count = 0

for i in range(1,Num+1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Total Number of Even is: {even_count}")
print(f"Total Number of Odd is: {odd_count}")