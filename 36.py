import threading
#threading gives access to Python's tools for running multiple pieces of code concurrently (in separate "threads")
import time
#time is used here just to simulate each chore taking a certain amount of time, via time.sleep()

#walk_dog takes 6 seconds (and also takes two parameters, first and last, used to build a name
def walk_dog(first, last):
    time.sleep(6)
    print(f"You finish walking {first} {last}")

#take_out_trash takes 2 seconds
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

#get_mail takes 4 seconds
def get_mail():
    time.sleep(4)
    print("You get mail")

#time.sleep(n) just pauses execution for n seconds — standing in for how long a real chore might actually take

#Creating and starting the threads
#threading.Thread(...) creates a new thread — think of it as a separate, independent "worker" that can run code in parallel with your main program
#target=walk_dog tells this thread which function to run.
#args=("Scooby", "Doo") provides the arguments that function needs (first="Scooby", last="Doo") — packaged as a tuple
#.start() actually begins running that thread.
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

#.join() tells the main program: "pause here and wait until this specific thread has completely finished running."
chore1.join()
chore2.join()
chore3.join()

#Final line
print("All chores ar complete!")

#These are commented out, so they don't run — but they hint at the comparison this code is meant to demonstrate. If you called these functions normally (without threading), Python would run them one at a time, in sequence: wait 6 seconds for walk_dog, then wait 2 more seconds for take_out_trash, then wait 4 more seconds for get_mail — a total of 12 seconds.
#walk_dog()
#take_out_trash()
#get_mail()
