
import numpy as np

arr = np.arange(1, 11)
print(arr)

print(arr.sum())
print(arr.mean())
print(arr.max())

arr_times_2 = arr * 2
print(arr_times_2)

arr_new = arr.copy()
arr_new[arr_new > 5] = 0

print(arr_new)



import pandas as pd

names = ["Arailym", "Alikhan", "Dimash", "Magzhan", "Ansar"]
ages = [18, 18, 24, 20, 19]
scores = [85, 90, 78, 88, 95]

data = {
    "Name": names,
    "Age": ages,
    "Score": scores
}

df = pd.DataFrame(data)

print("Full table:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

average = df["Score"].mean()
print("Average score:", average)

print("\nStudents older than 20:")
print(df[df["Age"] > 20])

print("\nStudents with score > 80:")
print(df[df["Score"] > 80])



import matplotlib.pyplot as plt

plt.plot(names, scores)
plt.show()

plt.bar(names, scores)
plt.show()
