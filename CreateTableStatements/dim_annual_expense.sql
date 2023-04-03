CREATE TABLE dim_annual_expense (
    location_id INTEGER,
    amount FLOAT,
    category VARCHAR(100),
    number_of_adults INTEGER,
    number_of_children INTEGER,
    number_of_working_adults INTEGER,
    snapshot_date DATE
)