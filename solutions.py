
import pandas as pd
import plotly.express as px
import pandas as pd
import plotly.express as px

def Exercise2() -> pd.DataFrame:
    """
    Analyzes the relationship between family size, passenger class, and ticket fare.
    Returns a table with total passengers, average, minimum, and maximum fares.
    """
    # Load dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv"
    )
    
    # --- Step 1: Create family size column ---
    df = df.copy()
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    # --- Step 2: Group by class and family size ---
    grouped = (
        df.groupby(["Pclass", "FamilySize"])["Fare"]
          .agg(TotalPassengers="count",
               AvgFare="mean",
               MinFare="min",
               MaxFare="max")
          .reset_index()
    )

    # --- Step 3: Sort for readability ---
    grouped = grouped.sort_values(by=["Pclass", "FamilySize"]).reset_index(drop=True)

    return grouped


print(Exercise2())