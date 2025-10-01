# Importing necessary libraries
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## EXERCISE 1: SURVIVAL PATTERNS

# Load the Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
"""
    Analyzing survival patterns based on passenger demographics

    demographic categories: class, sex, age group

    Returns: Table with results of all combinations of demographic categories
"""

# 1) Create a new column in the Titanic dataset that classifies passengers into age categories: 'Child' (0-12), 'Teen' (13-19), 'Adult' (20-59), and 'Senior' (60+)
"""
    Defining age categories using pd.cut
    Using pd.cut to cut the 'age column into bins and creating a new column 'Age_group' by adding labels to the bins

    age bins = [0, 12, 19, 59, np.inf]
    labels = ['Child', 'Teen', 'Adult', 'Senior']
"""
df['Age_group'] = pd.cut(df['Age'], bins=[0, 12, 19, 59, np.inf], labels=['Child', 'Teen', 'Adult', 'Senior'])

# 2) Group the passengers by class, sex, and age group
"""
    Use groupby to group the passengers
"""
grouped = df.groupby(['Pclass', 'Sex', 'Age_group'])

# 3) For each group, calculate the total number of passengers, survivors, and survival rate
"""Use agg to aggregate the grouped data
    Calculating total passengers(n_passengers), survivors(n_survivors), and survival rate(survival_rate)
"""
summary = grouped.agg(
    n_passengers=('Survived', 'count'),
    n_survivors=('Survived', 'sum')
).reset_index()
summary['survival_rate'] = summary['n_survivors'] / summary['n_passengers']





