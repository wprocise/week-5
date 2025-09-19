import streamlit as st

from apputil import *


st.write(
'''
# Week x: [Title]

...
''')

st.write(
'''
# Week 5: Titanic Survival Visualization

Explore survival rates by class and gender.
'''
)

# Load Titanic dataset

# Generate and display the figure
fig = plot_survival_by_age_class_gender()
st.plotly_chart(fig, use_container_width=True)
