Num = [12,14,13,19,17,30,40]

# Num = [1,2,3,4,5,6,7]

for i in range(len(Num)-1):
    if Num[i] < Num[i+1]:
        continue
    else:
        print("Not Sorted")
        break

else:
    print("Your list is sorted")