import pandas as pd
import datetime

print("Starting data job...")

data={"name": ["Priya", "John"], "age": [25,30]}
df=pd.DataFrame(data)

print(df)

with open("output.txt", "a") as f:
    f.write("Run at: " + str(datetime.datetime.now()) + "\n")