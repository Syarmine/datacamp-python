# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, val in cars.iterrows():
    print(lab)
    print(val)