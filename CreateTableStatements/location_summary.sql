CREATE TABLE location_summary (
    zip_code VARCHAR(10),
    state VARCHAR(2),
    county VARCHAR(100),
    recommended_annual_salary FLOAT,
    average_annual_salary FLOAT,
    expense_score FLOAT,
    crime_score FLOAT,
    avg_home_price FLOAT,
    avg_home_age FLOAT,
    avg_square_footage FLOAT,
    snapshot_date DATE
)