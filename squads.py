from pathlib import Path
import pandas as pd
import json


SQUADS_FILE = Path(
    r"C:\Users\darth\OneDrive\Documents\Data\worldcup.squads.json"
)


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", 50)




def fetch_squads():

    with open(SQUADS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []

    for team in data:
        team_name = team.get("name")
        fifa_code = team.get("fifa_code")
        group = team.get("group")

        players = team.get("players", [])

        for p in players:
            rows.append(
                {
                    "team": team_name,
                    "fifa_code": fifa_code,
                    "group": group,
                    "player_number": p.get("number"),
                    "position": p.get("pos"),
                    "player_name": p.get("name"),
                    "date_of_birth": p.get("date_of_birth"),
                    "club_name": p.get("club", {}).get("name"),
                    "club_country": p.get("club", {}).get("country"),
                }
            )

    df = pd.DataFrame(rows)

    print("Loaded squads:", df.shape)

    return df


def clean_squads(df):

    df = df.dropna(axis=1, how="all")

    preferred_order = [
        "team",
        "fifa_code",
        "group",
        "player_number",
        "position",
        "player_name",
        "date_of_birth",
        "club_name",
        "club_country",
    ]

    cols = [c for c in preferred_order if c in df.columns]

    return df[cols]


def preview_squads(df):

    print(
        df.head(20).to_string(index=False)
    )
