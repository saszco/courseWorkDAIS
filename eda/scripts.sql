SELECT
main.dim_region_data.region_name,
main.dim_year.year,
main.cancer_analysis.death_cases_count,
main.cancer_analysis.disease_cases_count,
main.cancer_analysis.crude_death_rate,
main.cancer_analysis.crude_disease_rate,
main.dim_pollution.source_name,
main.cancer_analysis.pollution_count
FROM main.cancer_analysis
INNER JOIN main.dim_region_data ON main.cancer_analysis.region_info = main.dim_region_data.region_id
INNER JOIN main.dim_year ON main.cancer_analysis.year_info = main.dim_year.year_id
INNER JOIN main.dim_pollution ON main.cancer_analysis.pollution_info = main.dim_pollution.pollution_id
ORDER BY main.dim_region_data.region_name