import plotly.express as px
import pandas as pd

def exercise1():
    """
    Returns a DataFrame with survival counts and survival rates
    grouped by passenger class and sex.
    """
    # Load the Titanic dataset from the given URL
    df = pd.read_csv("https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv")
    # Group the data by passenger class and sex, and focus on the Survived column
    grouped = (
        df.groupby(["Pclass", "Sex"])["Survived"]
          # Count the total passengers and sum the survivors
          .agg(["count", "sum"]) 
          # Reset the index so Pclass and Sex are columns
          .reset_index()
          # Rename the columns to Total and Survived
          .rename(columns={"count": "Total", "sum": "Survived"})
    )
    # Calculate the survival rate for each group
    grouped["SurvivalRate"] = grouped["Survived"] / grouped["Total"]
    # Return the final table
    return grouped
def exercise1_visualize():
    return 

def exercise2():
    """
    Returns a DataFrame with survival counts and survival rates
    grouped by passenger class and sex.
    """
    # Load the Titanic dataset from the given URL
    df = pd.read_csv("https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv")
    # Group the data by passenger class and sex, and focus on the Survived column
    grouped = (
        df.groupby(["Pclass", "Sex"])["Survived"]
          # Count the total passengers and sum the survivors
          .agg(["count", "sum"]) 
          # Reset the index so Pclass and Sex are columns
          .reset_index()
          # Rename the columns to Total and Survived
          .rename(columns={"count": "Total", "sum": "Survived"})
    )
    # Calculate the survival rate for each group
    grouped["SurvivalRate"] = grouped["Survived"] / grouped["Total"]
    # Return the final table
    return grouped
def exercise2_visualize():
    return 

def exercise3():
    """
    Analyzes the relationship between family size, passenger class, and ticket fare.
    Returns a table with total passengers, average, minimum, and maximum fares.
    """
    # Load dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv"
    )
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    # Group by class and family size
    grouped = (
        df.groupby(["Pclass", "FamilySize"])["Fare"]
          .agg(TotalPassengers="count",
               AvgFare="mean",
               MinFare="min",
               MaxFare="max")
          .reset_index()
    )
    # Sort for readability
    grouped = grouped.sort_values(by=["Pclass", "FamilySize"]).reset_index(drop=True)

    return grouped
def exercise3_visualize():
    return