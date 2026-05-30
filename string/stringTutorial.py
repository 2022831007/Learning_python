# we can express it as single quote,double quote,triplle quote
str1="this is a string"
str2='apna college'
str3="""this is a string"""

# to print string next line we use escape sequence character

str4="this is a string.\n we are creating it in python"
print(str4)
# for tab space we use \t
str4="this is a string.\t we are creating it in python"
print(str4)

# concatination
print(str1+str2)
final_str=str1+" "+str2
print(final_str)
# length of str
print(len(str1))
len2=len(str2)
print(len2)

# indexing
ch=str1[0]
ch2=str1[2]
print(ch2)

# slicing:accesing part of the string
print(str2[0:5])
print(str2[5:12])
print(str2[5:len(str2)]) #same output as before
print(str2[5:]) #python will automatic give the last index or first index
print(str2[:5])

#slicing in negative index,which means backwords
str="apple"
print(str[-3:-1]) #pl
print(str[-5:-2]) #app

#string funtions
str="i am studing from  python from yt"
print(str.endswith("on"))
print(str.capitalize()) #to capitalize the first character,it will works as once,never change the original string
print(str)
#if we want to change the original string to capitalize
str=str.capitalize()
print(str)

print(str.replace("o","a")) #replace old value to new value
print(str.replace("python","js")) #replace substring which are a form of replace old value to new value
#find use to if a word exist in string or not
print(str.find("am")) #return the first index of the word
print(str.find("q")) #return -1,as not exist this string
print(str.count("from")) #count the occurance of the substring
print(str.count("o"))