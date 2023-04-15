CREATE TABLE summary_zip_code (
    zip_code VARCHAR(20),
    state VARCHAR(2),
    county VARCHAR(100),
    recommended_annual_salary FLOAT,
    average_annual_salary FLOAT,
    expense_score FLOAT,
    crime_score FLOAT,
    average_home_price FLOAT,
    average_home_age_in_years FLOAT,
    average_square_footage FLOAT,
    average_price_per_square_foot FLOAT,
    average_time_on_market_in_days FLOAT,
    snapshot_date DATE DEFAULT CURRENT_DATE()
)