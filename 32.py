import json
import csv

txt_data = "I like pizza "

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

#For text data, there are different modes as well
# w is for write
# If we use x, we'll write a file if that file doesn't already exist, in this case, it does
#There's also a to append. Any new data will be appended to that file.

file_path = "C:/Users/DELL/Desktop/output.csv"

#So when working with file paths, it could be a relative file path or an absolute file path.

#With is a statement. It's used to wrap a block of code to execute. If we open a file, the with statement also closes that file when we're done with it so we don't need to manually close files. When you open a file it is good practice to close it.
#The open function (open(file_path, "w")) will return a file object. The first parameter(file_path,) is the file path, the second parameter("w") is the mode.
# w is write
# x will also write if this file doesn't exist. If it already does exist, we'll receive an error.
# a is for append, to append a file.
# r is to read.


# a .json file is made of key value pairs
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

            #The csv file is made of comma seperated values
            
        #json.dump(employees, file, indent=4)
        #print("Json file was created")

        #a dictionary or anything that uses key value pairs is a great candidate to be output to a json file.
        #for employee in employees:
            #file.write(employee + "\n")

        print(f"txt file '{file_path}' was created")
        #We also have the capability of setting an absolute file path.
except FileExistsError:
    print(f"File '{file_path}' already exists")
