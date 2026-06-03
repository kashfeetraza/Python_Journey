age = [2000,14,9,3000,9,11,15,19,900]

largest = age[0]
index = 0

for i in range(len(age)):
    # print(i)
    if age[i] > largest:
        largest = age[i]
        index = i

print(f"Your largest Number Value is {largest} at index {index}")