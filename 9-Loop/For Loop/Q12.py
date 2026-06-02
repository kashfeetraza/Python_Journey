str1 = "P@#yn26at^&i5ve"

Total_letter = len(str1)

print(f"Total letters is {Total_letter}")

Total_char = 0
Total_digits = 0
Total_symbol = 0

for i in range(Total_letter):
    ascii_value = ord(str1[i])

    if (32 <= ascii_value <= 47) or (58 <= ascii_value <= 64) or (91 <= ascii_value <= 96) or (123 <= ascii_value <= 126):
        Total_symbol += 1
    elif (48 <= ascii_value <= 57):
        Total_digits += 1
    else:
        Total_char +=1
print(f"Total symbol is {Total_symbol}")
print(f"Total Digits is {Total_digits}")
print(f"Total Character is {Total_char}")