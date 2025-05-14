CREATE TABLE IF NOT EXISTS main.dim_region_data (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(255) NOT NULL,
    population_count INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_pollution (
    pollution_id SERIAL PRIMARY KEY,
    source_name VARCHAR(255) NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    pollutant_type_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_year (
    year_id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS main.cancer_analysis (
    id SERIAL PRIMARY KEY,
    region_info INTEGER NOT NULL REFERENCES main.dim_region_data(region_id),
    year_info INTEGER NOT NULL REFERENCES main.dim_year(year_id),
    death_cases_count INTEGER NOT NULL,
    disease_cases_count INTEGER NOT NULL,
    crude_death_rate NUMERIC(5, 2) NOT NULL,
    crude_disease_rate NUMERIC(5, 2) NOT NULL,
    pollution_info INTEGER NOT NULL REFERENCES main.dim_pollution(pollution_id),
    pollution_count NUMERIC(5, 2) NOT NULL
);
