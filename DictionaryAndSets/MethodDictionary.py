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
print(info.keys())
#typecast
print(list(info.keys())) #convert the dictionary into list
print(len(info)) #length of the dictionary

print(len(list(info.keys()))) #length of the lists
print(info.values()) #print all the values of dic
print(info.items()) #return the pairs as tuples
print(list(info.items()))
pairs = list(info.items())
print(pairs[0]) #access the first tuple or pair of the dictionary 
print(pairs[1])
#get method return the value of the key
print(info["name"]) 
print(info.get("name"))
#print(info["name2"]) #return errror
print(info.get("name2")) #dont return error
#update method
info.update({"city":"Sherpur"})
print(info)
new_dic={"cgpa":"3.58"}
info.update(new_dic)
print(info)