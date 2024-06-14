import os

#FILE HANDLING

#1.OPENING FILE
#open the file using the open() function, takes 2 parametersm filename and mode
#1.1 using open()
file_object = open('sample.txt', 'r')

#1.2 using with
with open('sample.txt', 'r') as file:
    file.read()
    #do something

#2. READING FROM A FILE 
print("--------------READING FROM A FILE----------------")
print(file_object.read())
file_object.close()

#reading the first ten characters of the file
print("--------------reading the first ten characters of the file------------------")
file_object = open('sample.txt', 'r')
print(file_object.read(10))
file_object.close()

#readline() returns one line
print("---------------readline() returns one line-------------")
file_object = open('sample.txt', 'r')
print(file_object.readline())
file_object.close()

#readlines() reads all lines into the list
print("-------------readlines() reads all lines into the list----------")
file_object = open('sample.txt', 'r')
print(file_object.readlines())
file_object.close()

#loop through the file line by line
print("-------------loop through the file line by line----------")
file_object = open('sample.txt', 'r')
for line in file_object:
    print(line)
file_object.close()
# 3. WRITING TO A FILE
# writing to an existing file
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# using the append mode
print("------------using the append mode-----------")
file_object = open("Example1.txt", "a")
file_object.write("\nNow the file has more content!")
print(file_object)
file_object.close()

# using the write mode
print("------------using the write mode------------")
file_object = open("test1.txt", "w")
file_object.write("Woops! I have deleted the content!")

# Create a New File
# To create a new file, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# using the x mode 
print("--------------using the x mode---------------")
f = open("sampleData.txt", "x")     #new empty file is created
f.write("I have created a new file")

# using the a mode
print("--------------using the a mode--------------")
f = open("sampleData1.txt", "a")     #new empty file is created
f.write("\nHello World")             #new content is added

# using the w mode 
f = open("sampleData2.txt", "w")     #new empty file is created
f.write("Hello World")               #new content is added

# CLOSING THE FILE
file_object.close()


# DELETING THE FILE
# delete the file using .remove() from the os module
os.remove("file.txt")

# check if the file exists before deleting it to avoid errors
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("File does not exist")

# remove directory
# only empty folders can be removed
os.rmdir("test")