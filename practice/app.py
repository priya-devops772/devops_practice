#print("Hello from DevOps")
# name = "Priya"
#name = input("Enter your name: ")
# print(f"Hello {name},your script is running!")
#print(f"Welcome {name} to DevOps world!")

# import datetime

# print("Running data job...")
# print("Time:",datetime.datetime.now())
# print("DevOps test")
# a=5
# b=7
# print(a * b)

import datetime

with open("output.txt", "a") as f:
    f.write("Run at: " + str(datetime.datetime.now()) + "\n")