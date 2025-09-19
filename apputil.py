import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')


import pandas as pd

def survival_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns survival statistics grouped by Age, Pclass, and Sex.
    Demonstrates Week 3 (groupby, agg, sorting) and Week 4 (categorical binning).
    """

    # --- Week 4: use pd.cut to group ages into categories ---
    bins = [-1, 12, 19, 59, 150]  
    labels = ["Child", "Teen", "Adult", "Senior"]
    df = df.copy()
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

    # --- Week 3: groupby + agg for totals and survival counts ---
    grouped = (
        df.groupby(["Pclass", "Sex", "AgeGroup"])["Survived"]
          .agg(Total="count", Survived="sum")
          .reset_index()
    )

    # --- Week 3: create new column for rate ---
    grouped["SurvivalRate"] = grouped["Survived"] / grouped["Total"]

    # --- Week 3: sort values for readability ---
    grouped = grouped.sort_values(by="Pclass")

    return grouped

def plot_survival_by_age_class_gender():
    """
    Creates a Plotly bar chart showing survival rate by AgeGroup, Sex, and Pclass.
    """
    data = survival_stats(df)

    fig = px.bar(
        data,
        x="AgeGroup",
        y="SurvivalRate",
        color="Sex",
        barmode="group",
        facet_col="Pclass",
        template="plotly_white",
        text="SurvivalRate"  # add numbers on bars
    )

    # --- Make it look nice ---
    fig.update_layout(
        title="Titanic Survival Rates by Age Group, Class, and Gender",
        yaxis=dict(title="Survival Rate", tickformat=".0%"),
    )

    return fig
print(survival_stats(df))
print("---------------")
print(df)