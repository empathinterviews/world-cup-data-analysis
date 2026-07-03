from pathlib import Path
import psycopg2

# PostgreSQL Connection

DB_NAME = "world_cup_db"
DB_USER = "postgres"
DB_PASSWORD = "Blu3@rr0w4"
DB_HOST = "localhost"
DB_PORT = "5432"

OUTPUT_DIR = Path(
    r"C:\Users\darth\world-cup-data-analysis\Output"
)


# Helper Function

def copy_csv(cursor, table_name, csv_path):

    print(f"Loading {table_name}...")

    with open(csv_path, "r", encoding="utf-8") as f:

        cursor.copy_expert(
            f"""
            COPY {table_name}
            FROM STDIN
            WITH (
                FORMAT CSV,
                HEADER TRUE,
                DELIMITER ','
            );
            """,
            f
        )

    print(f"✓ {table_name} loaded.")


# Main
def main():

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cur = conn.cursor()

    try:

        copy_csv(cur, "teams", OUTPUT_DIR / "teams.csv")

        copy_csv(cur, "groups", OUTPUT_DIR / "groups.csv")

        copy_csv(cur, "stadiums", OUTPUT_DIR / "stadiums.csv")

        copy_csv(cur, "squads", OUTPUT_DIR / "squads.csv")

        copy_csv(cur, "matches", OUTPUT_DIR / "matches.csv")

        copy_csv(cur, "qualifiers_matches",
                 OUTPUT_DIR / "qualifiers_matches.csv")

        copy_csv(cur, "goals", OUTPUT_DIR / "goals.csv")

        conn.commit()


    except Exception as e:

        conn.rollback()

        print("\nLoad failed.")
        print(e)

    finally:

        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
