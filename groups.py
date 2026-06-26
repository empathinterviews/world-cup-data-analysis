from pathlib import Path
import pandas as pd
import json

BASE_DIR = Path(
    r"C:\Users\darth\OneDrive\Documents\Data\worldcup.groups.json"
)


def fetch_groups():

    with open(BASE_DIR, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Flatten groups -> teams
    df = pd.json_normalize(
        data,
        record_path=["groups", "teams"],
        meta=[
            "name",
            ["groups", "name"]
        ]
    )

    df.columns = [
        "team",
        "tournament",
        "group"
    ]

    print("Loaded groups:", df.shape)

    return df


def clean_groups(df):

    return df.dropna(axis=1, how="all")


def preview_groups(df):

    print(
        df.head(20).to_string(index=False)
    )
