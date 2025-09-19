import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''
# Titanic Visualization 1

'''
)
# Generate and display the figure
fig = exercise1_visualize()
st.plotly_chart(fig, use_container_width=True)

st.write(
'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
fig2 = exercise2_visualize()
st.plotly_chart(fig, use_container_width=True)

st.write(
'''
# Titanic Visualization 3
'''
)
# Generate and display the figure
fig2 = exercise3_visualize()
st.plotly_chart(fig, use_container_width=True)