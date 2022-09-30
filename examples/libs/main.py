import numpy as np 
import pandas as pd

elements = np.random.randint(0, 10, 15)

print(elements)

user1 = ["John", 15, 1.80]
user2 = ["Abraham", 35, 1.80]
user3 = ["WD", 23, 1.80]

userClass = [user1, user2, user3]

userColumns = ["name", "age", "height"]
userLines = ["#1", "#2", "#3"]

df = pd.DataFrame(data=userClass, index=userLines, columns=userColumns)
print(df)