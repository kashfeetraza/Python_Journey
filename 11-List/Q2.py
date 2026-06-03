age = [20,14,9,3,9,11,15,19]

age_length = len(age)
total_score = 0

# print("Positive Age limit:")
for i in age:
     total_score += i

mean_of_list = total_score/age_length

print(mean_of_list)