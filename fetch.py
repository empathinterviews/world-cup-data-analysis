from pathlib import Path
import pandas as pd
import json


BASE_DIR = Path(
    r"C:\Users\darth\OneDrive\Documents\Data\worldcup.json-master"
)

# Cleaner pandas output
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 50)


def fetch_matches(year):
    """
    Load and flatten one World Cup matches dataset.
    """

    file_path = BASE_DIR / str(year) / "worldcup.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Flatten matches JSON
    df = pd.json_normalize(
        data,
        record_path=["matches"],
        meta=["name"]
    )

    # Add tournament year
    df["year"] = year

    print(f"Loaded {year}: {df.shape}")

    return df


def fetch_all_matches():
    

    world_cup_years = [
        1930, 1934, 1938,
        1950, 1954, 1958,
        1962, 1966, 1970,
        1974, 1978, 1982,
        1986, 1990, 1994,
        1998, 2002, 2006,
        2010, 2014, 2018,
        2022, 2026
    ]

    dfs = []

    for year in world_cup_years:

        try:
            dfs.append(fetch_matches(year))

        except FileNotFoundError:
            print(f"Missing data for {year}")

    matches = pd.concat(
        dfs,
        ignore_index=True
    )

    print(f"\nTotal matches loaded: {matches.shape}")

    return matches


def explode_goals(df):

    # Team 1 goals

    home = df[
        [
            "year",
            "date",
            "team1",
            "team2",
            "goals1"
        ]
    ].copy()

    home["scoring_team"] = home["team1"]

    home = home.explode("goals1")

    home = home.dropna(
        subset=["goals1"]
    )

    home_details = pd.json_normalize(
        home["goals1"]
    )

    home = (
        home
        .drop(columns=["goals1"])
        .reset_index(drop=True)
        .join(home_details)
    )



    # Team 2 goals

    away = df[
        [
            "year",
            "date",
            "team1",
            "team2",
            "goals2"
        ]
    ].copy()

    away["scoring_team"] = away["team2"]

    away = away.explode("goals2")

    away = away.dropna(
        subset=["goals2"]
    )

    away_details = pd.json_normalize(
        away["goals2"]
    )

    away = (
        away
        .drop(columns=["goals2"])
        .reset_index(drop=True)
        .join(away_details)
    )

    # Combine both teams
    goals = pd.concat(
        [
            home,
            away
        ],
        ignore_index=True
    )

    return goals


def clean_matches(df):

    df = df.dropna(
        axis=1,
        how="all"
    )

    return df


def preview_matches(df):

    print(
        df[
            [
                "year",
                "date",
                "team1",
                "team2",
                "score.ft",
                "ground"
            ]
        ]
        .head(20)
        .to_string(index=False)
    )


def preview_goals(df):


    print(
        df[
            [
                "year",
                "date",
                "scoring_team",
                "name",
                "minute"
            ]
        ]
        .head(20)
        .to_string(index=False)
    )
