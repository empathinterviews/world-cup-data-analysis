from pathlib import Path
import pandas as pd
import fetch as ft
import teams
import groups
import qualifiers as qf
import squads
import stadiums

# Output folder
OUTPUT_DIR = Path(
    r"C:\Users\darth\world-cup-data-analysis\Output"
)


if __name__ == "__main__":


    # MATCHES PIPELINE

    matches = ft.fetch_all_matches()

    #Cleaning matches
    matches = ft.clean_matches(matches)

    #Building goal-level dataset
    goals = ft.explode_goals(matches)

    #Preview Matches
    ft.preview_matches(matches)

    #Goal Data Preview
    ft.preview_goals(goals)

    matches.to_csv(
        OUTPUT_DIR / "matches.csv",
        index=False
    )

    goals.to_csv(
        OUTPUT_DIR / "goals.csv",
        index=False
    )


    # TEAMS PIPELINE

    team_df = teams.fetch_teams()

    team_df = teams.clean_teams(team_df)

    #Teams Preview
    teams.preview_teams(team_df)

    team_df.to_csv(
        OUTPUT_DIR / "teams.csv",
        index=False
    )


    #Loading groups data
    group_df = groups.fetch_groups()
    group_df = groups.clean_groups(group_df)


    #Groups Preview
    groups.preview_groups(group_df)

    group_df.to_csv(
        OUTPUT_DIR / "groups.csv",
        index=False
    )



    # QUALIFIERS PIPELINE

    #Loading qualifiers data
    qualifiers = qf.fetch_qualifier_matches()


    #Cleaning qualifiers
    qualifiers = qf.clean_qualifiers(qualifiers)

    #Preview qualifiers
    qf.preview_qualifiers(qualifiers)

    qualifiers.to_csv(
        OUTPUT_DIR / "qualifiers_matches.csv",
        index=False
    )

    #Loading squads data
    squads_df = squads.fetch_squads()
    squads_df = squads.clean_squads(squads_df)

    #Squads Preview
    squads.preview_squads(squads_df)

    squads_df.to_csv(
        OUTPUT_DIR / "squads.csv",
        index=False
    )

    #Loading stadiums data
    stadium_df = stadiums.fetch_stadiums()
    stadium_df = stadiums.clean_stadiums(stadium_df)

    #Stadiums Preview
    stadiums.preview_stadiums(stadium_df)

    stadium_df.to_csv(
        OUTPUT_DIR / "stadiums.csv",
        index=False
    )
