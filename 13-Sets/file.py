# st = "Kashfeet"
# a = hash(st)
# print(a)

# st = {1,2,"Hello",11,14,"Kaf",10,3,4,5,6}

# for i in st:
#     print(i)

# st.add(50)
# st.remove(4)

# st.pop()
# st.clear()
A = {1,2,3,4,5,6}
B = {4,7,8,9}
# Union = A.union(B)
Union = A | B
# intersection = A.intersection(B)
intersection = A & B
# Difference = A.difference(B)
Difference = A - B
# Symmetic_Difference = A.symmetric_difference(B)
Symmetic_Difference = A ^ B
print("Intersection: ",intersection)
print("Union: ",Union)
print("Difference: ",Difference)
print("Symmetric Difference: ",Symmetic_Difference)