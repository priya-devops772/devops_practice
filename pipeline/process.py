import pandas as pd

print("Starting job...")

df=pd.read_csv("input.csv")

df["age_after_5_years"] = df["age"] + 5

print(df)

df.to_csv("output.csv", index=False)

print("Pipeline completed!")