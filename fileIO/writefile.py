f = open("fileIO/demo.txt", "a")
f.write("then i will move to reactjs.\n")
f.close()

print("Done")
#read+write
f = open("fileIO/demo.txt", "r+")
f.write("abc")
f.close()
