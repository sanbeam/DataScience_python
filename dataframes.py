import pandas as pd
data = {"periods":["Maths", "Science", "English"],
"duration_in_hrs": [1, 2, 0.5]}
df = pd.DataFrame(data)
print(df)

print(df.loc[0])