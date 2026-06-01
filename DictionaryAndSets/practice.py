#ques-1:store following word in a python dictionary
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"]

}
print(dictionary)
#ques-2:you given a list of subjects for students.Assume one classroom is required for 1 subject.How many classroms are needed by all students
subjects={"python","java","C++","js","java","python","java","C++","C"}
print("classroom needed:",len(subjects))
#ques-3:write a program to enter marks of 3 subjects from the user and store them in a dictionary
#start with an empty dictionary and add one by one ,use subject name as key and marks as values
dic={}
for i in range(3):
     subjects=input("Enter your subject name: ")
     marks=int(input("enter your marks : "))
     dic[subjects]=marks


print(dic)
#figure out a way to store 9 &9.0 as separate values in the set
#(you can yake help of built in data types
values={9,"9.0"}
print(values)
#another way
values={
    ("float",9.0),
    ("int",9)
}
print(values)