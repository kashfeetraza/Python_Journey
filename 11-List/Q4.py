Num = [12,14,13,19,17,30,40]


largest = Num[0]
Sec_large = Num[0]
index = 0

for i in Num:
    if i > largest:
         Sec_large = largest
         largest = i
         
    elif i > Sec_large:
         Sec_large = i

print(f"Largest =  {largest}")
print(f"Sec Largest =  {Sec_large}")