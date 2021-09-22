import pandas as pd
import numpy as np

data = pd.ExcelFile("C:/Users/Miles/Downloads/dls_books.xlsx")
schedule = pd.read_excel(data, "Schedule Numbers", header=2).drop(columns=["Unnamed: 0", "Unnamed: 2", "Unnamed: 4", "Unnamed: 6"])
print(schedule)
print(schedule['Number'])
print(schedule['Service Date'])
print(schedule['Client '])
s = schedule.to_numpy()
print(s)
