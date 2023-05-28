CREATE TABLE dim_location (
    location_id integer autoincrement start 1 increment 1,
    zip_code VARCHAR(20),
    state VARCHAR(2),
    county VARCHAR(60),
    latitude FLOAT,
    longitude FLOAT
)