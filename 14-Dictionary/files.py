# dic = {1 : "Kashfeet",2 : 24,3 : "Kashfeet"}
# dic = {10:100 , 20:200, 30:300}

# dic2 = dic.copy()
# dic2[10] = 500

# print(dic)
# print(dic2)

# print(dic[10])

# dic[10] = 10000


# dic.update({50:500})
# dic[50] = 500
# del dic[20]

# for i in dic.values():
    # print(dic[i])
    # print(i)


# print(dic)
 
# Deep Copy

# a = [1,2,3,4,5]
# b = a.copy()
# b[0] = 100

# print(a)
# print(b)

# help(dict)

# dic = {10:100 , 20:200, 30:300}

# dic2 = dic.get(20)
# print(dic2)

# print(dic.items())

# print(help(dict))

thisdict =	{
  "brand": "Suzuki",
  "model": "Alto",
  "year": 2008,
  "color": ["red","white","black"]
#   "year": 2020
}
dict_by_method = dict(name = "Kashfeet",age = 19,country = "Pak")

# print(len(thisdict))
# print(thisdict)
# print(thisdict["year"])
# print(type(thisdict))
# print(dict_by_method)

get_year_by_dict =thisdict.get("year")
# print(get_year_by_dict)


keys_in_dict = thisdict.keys()
# print(keys_in_dict)


# Add keys Manually
# print("Before:",thisdict)
thisdict["Zero Meter"] = True
# print("After:",thisdict)




Getting_value = thisdict.values()
# print(Getting_value)

Getting_items = thisdict.items()
# print(Getting_items)


# checking the value are exist in dictionary
# if "year" in thisdict:
    # print("Yes its Exist")

thisdict.update({"year": 2020})
# print(thisdict["year"])


thisdict.update({"Condition": "New"})
# print(thisdict)

# thisdict.pop("model")
# print(thisdict)


thisdict.popitem()
print(thisdict)
