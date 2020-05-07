pyto = open("test open file.txt", "r")
print(pyto.read())
pyto.close()
# First of perethesis is which file you want to open .
# Second part is what mode so for read mode is r, write mode is w, append mode is a, read and write mode is r+
# Always close the file when you open it
# Whether the file is readable or not this is the command to check it
print("=========================================================================================================")
pyto = open("test open file.txt", "r")
print(pyto.readline()) # This is to print individual line. as many times you type as many times it will print
print(pyto.readline())
print(pyto.readlines()) # difference is it made it in list.. as you can see when you run the program
pyto.close()
print("=========================================================================================================")
pyto = open("test open file.txt", "r")
for looping in pyto.readlines():
    print(looping)
pyto.close() # you can also use for loop to open files
print("=========================================================================================================")
pyto = open("test open file.txt", "a")
pyto.write("Saturday and Sunday Close")
pyto.close()
# This is to appened the line at the end of the program.



