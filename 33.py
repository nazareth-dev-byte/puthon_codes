
#To import a .json file, we would need the help of a json module.
import json
#To read a csv file,we would import the csv module
import csv


file_path = "C:/Users/DELL/Desktop/output.csv"
#To read this file, we'll add a with block. With is a statement, it's gonna wrap a block of code within a context manager and it would close a file if we open it.
#We'll use the open function. the open function has two arguments, our file path(file_path) and a mode "r". The open function is going to return a file object which we would give a nick name of file.If we forgot to include the file extension, we'll ru into a file not found error

try:
    with open(file_path, "r") as file:
        # This should read the content of out csv file.
        content = csv.reader(file)
        for line in content:
            #If you need a specific column fromma csv file, you could use an index.
            print(line[2])
        # This should read the content of out json file.
        #content = json.load(file)
        #With the data of out json file, we could access a value given a key
        #content = file.read()
        #We're assigning content to teh file.read method
        print(content)
except FileNotFoundError:
    print("File not found")

    #What if we don't have permission to read this file ?
except PermissionError:
    print("Permission denied")
