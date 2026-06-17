with open("/Users/macbook/Desktop/python_learning/fileIO/demo.txt") as f:
      data = f.read()
      print(data)

#in with,we dont need to close the file,it will automticly close the file


with open("/Users/macbook/Desktop/python_learning/fileIO/demo.txt","w") as f:
      f.write("new data")