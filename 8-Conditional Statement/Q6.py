Temprature = int(input("Enter The Temprature: "))

# Cold_face = ord("U+1F976")

if Temprature <= 0:
    print("Freezing Atmostphere Cold")
elif Temprature <= 10 and Temprature > 0:
    print("Very Cold")
elif Temprature >= 11 and Temprature <= 20:
    print("Cold")
elif Temprature >= 21 and Temprature <= 30:
    print("Pleasant")
elif Temprature >= 31 and Temprature <= 40:
    print("Hot")
elif Temprature >= 41:
    print("Very Hot")
