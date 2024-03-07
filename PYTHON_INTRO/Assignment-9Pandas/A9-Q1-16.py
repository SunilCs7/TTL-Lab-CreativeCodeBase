import numpy as np
import pandas as pd

# Given data
data = {
    'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'],
    'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4],
    'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1. Create a DataFrame birds from this dictionary data which has the index labels.
birds = pd.DataFrame(data, index=labels)

# 2. Display a summary of the basic information about birds DataFrame and its data.
print(birds.info())

# 3. Print the first 2 rows of the birds dataframe
print(birds.head(2))

# 4. Print all the rows with only 'birds' and 'age' columns from the dataframe
print(birds[['birds', 'age']])

# 5. select [2, 3, 7] rows and in columns ['birds', 'age', 'visits']
print(birds.loc[['c', 'd', 'h'], ['birds', 'age', 'visits']])

# 6. select the rows where the number of visits is less than 4
print(birds[birds['visits'] < 4])

# 7. select the rows with columns ['birds', 'visits'] where the age is missing i.e NaN
print(birds[birds['age'].isnull()][['birds', 'visits']])

# 8. Select the rows where the birds is a Cranes and the age is less than 4
print(birds[(birds['birds'] == 'Cranes') & (birds['age'] < 4)])

# 9. Select the rows the age is between 2 and 4(inclusive)
print(birds[(birds['age'] >= 2) & (birds['age'] <= 4)])

# 10. Find the total number of visits of the bird Cranes
print(birds[birds['birds'] == 'Cranes']['visits'].sum())

# 11. Calculate the mean age for each different birds in dataframe.
print(birds.groupby('birds')['age'].mean())

# 12. Append a new row 'k' to dataframe with your choice of values for each column. Then delete that row to return the original DataFrame.
birds.loc['k'] = ['parrots', 2, 3, 'yes']
birds = birds.drop('k')

# 13. Find the number of each type of birds in dataframe (Counts)
print(birds['birds'].value_counts())

# 14. Sort dataframe (birds) first by the values in the 'age' in decending order, then by the value in the 'visits' column in ascending order.
print(birds.sort_values(by=['age', 'visits'], ascending=[False, True]))

# 15. Replace the priority column values with'yes' should be 1 and 'no' should be 0
birds['priority'] = birds['priority'].map({'yes': 1, 'no': 0})

# 16. In the 'birds' column, change the 'Cranes' entries to 'trumpeters'.
birds['birds'] = birds['birds'].replace('Cranes', 'trumpeters')

print(birds)
