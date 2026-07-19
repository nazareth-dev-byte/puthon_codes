#we'll place user's inputs in try blocks because it's considered dangerous and harmful code.

try:
    number = int(input("Enter a number: "))
    print(1/number)
    #If an exception happens, we'll move on to step 2. Subsequently following the try block, we'll add the except block.
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
    #Hence we've gracefully handled this exception.
    #This except block only handles Zero division errors so if the user entered a string, there'll still be an error which would lead to a break in the code so let's fix that by creating another exception to handle value error
except ValueError:
    print("Enter only numbers please! ")

#We can also decide to catch all exceptions. It's considered bad practice because it's too broad of a cause, it's considered good practice to tell the user what went wrong exactly.
except Exception:
    print("Something went wrong!")
#This way if the error isn't a value error or a zerod ivision error, then we'll execute the exception.

#Lastly we have the finally block which executes regardless of whether we have an exception or not.It's usually used for any sort of cleanup you'l want to do.

finally:
    print("Do some cleanup here")
