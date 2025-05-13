CREATE TABLE IF NOT EXISTS main.dim_region_data (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(255) NOT NULL,
    population_count INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_death_cases (
    death_case_id SERIAL PRIMARY KEY,
    death_count INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_disease_cases (
    disease_case_id SERIAL PRIMARY KEY,
    disease_count INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_crude_disease_rate (
    crude_disease_rate_id SERIAL PRIMARY KEY,
    disease_rate NUMERIC(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_crude_death_rate (
    crude_death_rate_id SERIAL PRIMARY KEY,
    death_rate NUMERIC(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS main.dim_pollution (
    pollution_id SERIAL PRIMARY KEY,
    source_name VARCHAR(255) NOT NULL,
    pollution_count NUMERIC(5, 2) NOT NULL,
    category_name VARCHAR(255) NOT NULL
);

ALTER TABLE main.dim_pollution
ADD COLUMN pollutant_type_name VARCHAR(255) NOT NULL

CREATE TABLE IF NOT EXISTS main.cancer_analysis (
    id SERIAL PRIMARY KEY,
    region_id INTEGER NOT NULL,
    death_case_id INTEGER NOT NULL,
    disease_case_id INTEGER NOT NULL,
    incidence_rate_id INTEGER NOT NULL,
    death_rate_id INTEGER NOT NULL,
    pollution_id INTEGER NOT NULL
)

ALTER TABLE main.cancer_analysis
ADD CONSTRAINT fk_region_id
FOREIGN KEY (region_id)
REFERENCES main.dim_region_data(region_id)

ALTER TABLE main.cancer_analysis
ADD CONSTRAINT fk_death_case_id
FOREIGN KEY (death_case_id)
REFERENCES main.dim_death_cases(death_case_id)

ALTER TABLE main.cancer_analysis
ADD CONSTRAINT fk_disease_case_id
FOREIGN KEY (disease_case_id)
REFERENCES main.dim_disease_cases(disease_case_id)

ALTER TABLE main.cancer_analysis
ADD CONSTRAINT fk_incidence_rate_id
FOREIGN KEY (incidence_rate_id)
REFERENCES main.dim_crude_disease_rate(crude_disease_rate_id)

ALTER TABLE main.cancer_analysis
ADD CONSTRAINT fk_death_rate_id
FOREIGN KEY (death_rate_id)
REFERENCES main.dim_crude_death_rate(crude_death_rate_id)

ALTER TABLE main.cancer_analysis
ADD CONSTRAINT fk_pollution_id
FOREIGN KEY (pollution_id)
REFERENCES main.dim_pollution(pollution_id)