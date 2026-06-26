from pathlib import Path
import pandas as pd
import json

STADIUMS_FILE = Path(
    r"C:\Users\darth\OneDrive\Documents\Data\worldcup.stadiums.json"
)


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 50)


def fetch_stadiums():
    """
    Load and flatten stadium dataset.
    One row = one stadium.
    """

    with open(STADIUMS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)


    stadium_list = data.get("stadiums", [])

    rows = []

    for s in stadium_list:
        rows.append(
            {
                "name": s.get("name"),
                "city": s.get("city"),
                "country_code": s.get("cc"),
                "timezone": s.get("timezone"),
                "capacity": s.get("capacity"),
                "coords": s.get("coords"),
            }
        )

    df = pd.DataFrame(rows)

    print("Loaded stadiums:", df.shape)

    return df


def clean_stadiums(df):

    df = df.dropna(axis=1, how="all")

    preferred_order = [
        "name",
        "city",
        "country_code",
        "timezone",
        "capacity",
        "coords",
    ]

    cols = [c for c in preferred_order if c in df.columns]

    return df[cols]


def preview_stadiums(df):

    print(
        df.head(20).to_string(index=False)
    )
