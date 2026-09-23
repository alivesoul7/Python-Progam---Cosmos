import pandas as pd

data = {
    "Name": ["Aarav","Rohan","Sujal","Bibek","Kiran"],
    "Score": [45,72,61,38,84]
}
df = pd.DataFrame(data)
    
max_score = df["Score"].max()
print(f"Maximum Score: {max_score}")

df.insert(2, "Passed", df["Score"] >= 50)
print(df)

total_passed_students = df["Passed"].sum()
print(f"Total Passed Students: {total_passed_students}" )

