"""There are two type of type conversions
1-Explicit
2-Implicit
"""

# Integer float string boolean
# 1-Explicit
interger = 100

Conversion_Into_String = str(interger)
# print(type(Conversion_Into_String))

String = "120"
Conversion_Into_Integer = int(String)
# print(type(Conversion_Into_Integer))


# Falsey value 
"""
False
0
0.0
""
()
[]
{}
"""

# 2-Implicit
#automatically python convert one datatype to another datatype
division = 12/4
print(division)
