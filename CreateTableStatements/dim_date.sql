CREATE TABLE dim_date (
    date_id INTEGER AUTOINCREMENT PRIMARY KEY,
    date DATE,
    day_of_week VARCHAR(3) -- MON, TUE, ect...
)