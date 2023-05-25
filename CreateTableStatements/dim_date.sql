CREATE TABLE dim_date (
    date_id INTEGER AUTOINCREMENT START 1 INCREMENT 1,
    date DATE,
    day_of_week VARCHAR(3) -- MON, TUE, ect...
)