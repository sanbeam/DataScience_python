import pandas as pd
data = {"Subjects":["Maths", "Science", "English"],
"Duration_in_hrs": [1, 2, 0.5]}
df = pd.DataFrame(data, index = ["first period", "second period", "third period"])
print(df)
print(df.loc["second period"])
