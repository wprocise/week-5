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

st.write("What are the most common last names among Titanic families, and how many families share each last name?"
'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
# 4) Write a function called `last_names()` that extracts the last name of each passenger from the `Name` column, and returns the count for each last name (i.e., a pandas series with last name as index, and count as value). Does this result agree with that of the data table above? Share your findings in your app using `st.write`.
def last_names(df):
	"""
	Extracting last names from the 'Name' column
	Using str.split to split the 'Name' column and extract the last name
	Using value_counts to count the occurrences of each last name
	"""
	df['Last_Name'] = df['Name'].str.split(',').str[0]
	last_name_counts = df['Last_Name'].value_counts()
	return last_name_counts
	fig2 = visualize_families()
	st.plotly_chart(fig2, use_container_width=True)

st.write("What are the most common last names among Titanic families, and how many families share each last name?")
"""
    Creating a function called 'visualize_families()' that creates a bar chart showing the most common last names among Titanic families and how many families share each last name
    The bar chart displays the count of each last name on the x-axis and the last names on the y-axis
    The chart is sorted in descending order to highlight the most common last names
"""

def visualize_families(df):
    last_name_counts = last_names(df.copy())
    last_name_counts.name = 'count'
    last_name_counts = last_name_counts.reset_index()
    last_name_counts = last_name_counts.rename(columns={'index': 'Last_Name'})
    fig2 = px.bar(last_name_counts.head(10), x='Last_Name', y='count',
                 title='Most Common Last Names Among Titanic Families',
                 labels={'Last_Name': 'Last Name', 'count': 'Count'},
                 color='count',
                 color_continuous_scale=px.colors.qualitative.Vivid)
    return fig2
fig2 = visualize_families(df)
fig2.show()

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)