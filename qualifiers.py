from pathlib import Path
import pandas as pd
import json


QUALIFIERS_FILE = Path(
    r"C:\Users\darth\OneDrive\Documents\Data\worldcup.quali_playoffs.json"
)


def fetch_qualifier_matches():

    with open(QUALIFIERS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.json_normalize(
        data,
        record_path=["matches"],
        meta=["name"]
    )

    df["tournament"] = "World Cup 2026 Qualifiers"

    print("Loaded qualifiers:", df.shape)

    return df


def clean_qualifiers(df):

    return df.dropna(axis=1, how="all")


def preview_qualifiers(df):

    print(
        df[[
            "date",
            "team1",
            "team2",
            "score",
            "ground"
        ]].head(20).to_string(index=False)
    )
