#dictionaries are used to store data values in key:value pairs
#they are unordered,mutable(changeable)and dont allow duplicate keys
info={
    "key":"value",
    "name":"fatema",
    "learning":"python",
    "age":22,
    "is_adult":True,
    "subjects":["python","c","java"],
    "topics":("dic","set"),
    12:94.5,
    12.93: 34.56
}
print(info)
print(info["name"]) #access the dic value
print(info["topics"])
print(info["subjects"])
null_dic={}
print(null_dic)
print(type(null_dic))
null_dic["name"]="fatema"
print(null_dic)
