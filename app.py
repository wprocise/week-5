import streamlit as st

from apputil import *

st.write(
'''
# Week 5: Titanic Survival Visualization
Explore survival rates by class and gender.
'''
)

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Generate and display the figure
fig = plot_survival_by_age_class_gender()
st.plotly_chart(fig, use_container_width=True)

st.write(
'''
# Week 5: Titanic Visualization 2
'''
)

# Generate and display the figure
fig2 = exercise2()
st.plotly_chart(fig, use_container_width=True)