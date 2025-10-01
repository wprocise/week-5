import streamlit as st
from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# 6) Write a clear questions about the results from the table from the dataset
st.write("How did survival rates vary among different age groups on the Titanic?"
         
'''
# Titanic Visualization 1

'''
)
# 7) Create a Plotly visualization that addresses the question
# Generate and display the figure
def visualize_demographic():
	fig1 = px.bar(summary, x='Age_group', y='survival_rate',
			 title='Survival Rate by Age Group and Sex on the Titanic',
			 labels={'Age_group': 'Age Group', 'survival_rate': 'Survival Rate'},
			 color='Sex',
			 color_discrete_map={'male': 'blue', 'female': 'pink'},
			 barmode='group')
	return fig1

fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write(
'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)