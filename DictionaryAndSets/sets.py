#set is the collection of the unordered items
#each element in the set must be unique and immutable
#list and dic cant be store in sets as they are mutable
collection={1,2,3,4,"hello","world",2,2,4}
print(collection) # will print the once,not twice value,alawys unique values
print(type(collection))
print(len(collection)) #total number of items
coll={}#this is not set,this is empty dic
print(type(coll))
coll=set() #this is empty set
print(type(coll))
#Sets Methods
#sets mutable but the elements in the set is immutable
collection.add(5)
collection.add(6)
collection.add(8) #add the new value in the set
print(collection)
collection.remove(3) #remove an specific element in set
print(collection)
#we can add tuple,string also
collection.add("fatema")
collection.add((9,10,11))
print(collection)
#to clear e full set and make it empty we use clear()
#collection.clear() 
#print(collection) will return 0,as all element become empty
collection.pop() #removes a random value
print(collection)

#union and intersection methos
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2)) #print common value just
# this two method s will not chnage the original sets
print(set1)
print(set2)