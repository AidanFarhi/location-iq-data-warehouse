import os
import snowflake.connector
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # Initialize variables
    START_DATE = date(1600, 1, 1)
    END_DATE = date(2099, 12, 31)
    TABLE_NAME = "dim_date"
    BATCH_SIZE = 16_384  # Max number of expressions allowed by snowflake

    # Initialize a Snowflake connection
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USERNAME"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("WAREHOUSE"),
        database=os.getenv("DATABASE"),
        schema=os.getenv("SCHEMA"),
    )

    # Obtain a cursor to execute statements
    curs = conn.cursor()

    # Iterate from start date to end date and populate a list of (date, season) tuples
    dates_and_seasons = []
    current_date = START_DATE
    while current_date <= END_DATE:
        month = current_date.month
        day = current_date.day
        # Figure out the season
        if month in [1, 2, 3]:
            season = "SPRING" if month == 3 and day >= 20 else "WINTER"
        elif month in [4, 5, 6]:
            season = "SUMMER" if month == 6 and day >= 21 else "SPRING"
        elif month in [7, 8, 9]:
            season = "FALL" if month == 9 and day >= 22 else "SUMMER"
        elif month in [10, 11, 12]:
            season = "WINTER" if month == 12 and day >= 21 else "FALL"
        dates_and_seasons.append((str(current_date), season))
        current_date += timedelta(days=1)

    # Split the list into batches
    batches = [dates_and_seasons[i : i + BATCH_SIZE] for i in range(0, len(dates_and_seasons), BATCH_SIZE)]

    # Bulk insert dates and seasons in batches
    for batch in batches:
        curs.executemany(f"INSERT INTO {TABLE_NAME} (date, season) VALUES (%s, %s)", batch)
        conn.commit()

    # Close cursor and connection
    curs.close()
    conn.close()
