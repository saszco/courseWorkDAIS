CREATE TABLE IF NOT EXISTS stage.pollution_data (
    id SERIAL PRIMARY KEY,
    indicator VARCHAR(255),
    region_name VARCHAR(255),
    source_of_pollution VARCHAR(255),
    pollutant_type_name VARCHAR(255),
    source_category_name VARCHAR(255),
    periodicity VARCHAR(255),
    pollution_count INTEGER
);

CREATE TABLE IF NOT EXISTS stage.population (
    id SERIAL PRIMARY KEY,
    indicator VARCHAR(255),
    region_name VARCHAR(255),
    periodicity VARCHAR(255),
    population_count INTEGER
);

CREATE TABLE IF NOT EXISTS stage.cancer_disease_and_death (
    id SERIAL PRIMARY KEY,
    region_name VARCHAR(255),
    disease_case_count INTEGER,
    incidence_rate FLOAT,
    death_case_count INTEGER,
    death_rate FLOAT
);