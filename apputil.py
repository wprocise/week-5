# Importing necessary libraries
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## EXERCISE 1: SURVIVAL PATTERNS

# Load the Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# 1) Create a new column in the Titanic dataset that classifies passengers into age categories: 'Child' (0-12), 'Teen' (13-19), 'Adult' (20-59), and 'Senior' (60+)
