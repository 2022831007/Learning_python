#create a new file "practice.txt" using python.add the following data
# hi everyone 
# we are learning file i/o 
# using java
# i like programming in java


f= open("/Users/macbook/Desktop/python_learning/fileIO/practice.txt","a")
f.write("hi everyone\nwe are learning file i/o\nusing java\ni like programming in java")
f.close()

with open("/Users/macbook/Desktop/python_learning/fileIO/practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "Python")

with open("/Users/macbook/Desktop/python_learning/fileIO/practice.txt", "w") as f:
    f.write(new_data)

print(new_data)
#search if learning exist in the file or not

def check_for_word():
     with open("/Users/macbook/Desktop/python_learning/fileIO/practice.txt","r") as f:
      word="learning"
      data = f.read()
      if(data.find(word)!= - 1):
           print("found")
      else:
           print("not found")


check_for_word()

#check for line to found learning
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("/Users/macbook/Desktop/python_learning/fileIO/practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1    
    return -1


check_for_line()
#from a file containing numbers separated by comma,print the count of even numbers
with open("/Users/macbook/Desktop/python_learning/fileIO/prac2.txt","r") as f:
    data = f.read()

nums = data.split(",")

count = 0

for i in nums:
    if int(i) % 2 == 0:
        count += 1

print("Even numbers =", count)   
