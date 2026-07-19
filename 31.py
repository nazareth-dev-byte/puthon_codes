import os

file_path = "C:/Users/DELL/Desktop"
#This is an absolute file path.
#When working with strings, a backslash does serve as as an escape sequence.So we can either use double back slashes or foward slashes.
#And so this location exists

#To check to see of this file exists, I would use an if statement

if os.path.exists(file_path):#This method returns a boolean value of true or false id the file exists
    print(f"The location '{file_path}' exists'")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print(f"The location '{file_path}' does not exist")

    #We created a new directory and then put the test.txt file in it. So it's no longer next to our main file so this code would out that it doesn't exist.
    #With our relative file path, we'll have to navigate to our stuff folder then find the test file. so preceding the file name we'll add the stuff folder(check line 3). Then when we run it we get "The location 'stuff/test.txt' exists'"

    #For absolute file paths, on our desktop, we'll create a new file then we'll copy the location(check from line 3 to 6). If we get the location wrong, then the file no longer exists.

#There is a built in function of is_file to check to see if that function is in fact a file and not a directory.chack line 23

#and yeahh that is basic file detection using python
