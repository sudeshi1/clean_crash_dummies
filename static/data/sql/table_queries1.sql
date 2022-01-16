SELECT * FROM accidents;
SELECT * FROM people;
SELECT * FROM vehicle;

-- Displaying states where the most accidents occur
SELECT accidents.state, count(case_number) AS Accidents_Count
FROM accidents
GROUP BY accidents.state
ORDER BY Count (*) DESC;

-- Vehicle manufacturer and model with the most accidents
SELECT people.vehicle_model, people.vehicle_manufacturer, count (people.case_number) as Accidents_Count
FROM people
GROUP BY people.vehicle_model, people.vehicle_manufacturer
ORDER BY Count (*) DESC;

-- Most accidents by vehicle model in each state
SELECT accidents.state, people.vehicle_model, count (people.case_number) as Accidents_Count
FROM accidents
JOIN people
ON accidents.case_number = people.case_number
GROUP BY accidents.state, people.vehicle_model
ORDER BY Count (*) DESC;

-- Vehicle models and manufacturers with the most fatal accidents
SELECT vehicle_model, doa_status, vehicle_manufacturer, count (case_number) AS Accidents_Count
FROM people
WHERE doa_status = 'Fatal'
GROUP BY vehicle_model, doa_status, vehicle_manufacturer
ORDER BY Count(case_number) DESC;

-- Vehicle models and manufacturers with the most non-fatal accidents
SELECT vehicle_model, doa_status, vehicle_manufacturer, Count (case_number) AS Accidents_Count
FROM people
WHERE doa_status = 'No Fatality'
GROUP BY vehicle_model, doa_status, vehicle_manufacturer
ORDER BY Count(case_number) DESC;

-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
-- Breakdown of accidents by state by age
SELECT accidents.state, people.age, people.age_label, Count (accidents.case_number) AS Accidents_Count
FROM accidents
JOIN people
ON accidents.case_number = people.case_number
GROUP BY accidents.state, people.age, people.age_label
ORDER BY Count (*) DESC;

-- Age and Age group with the most accidents
SELECT people.age, people.age_label, Count (case_number) AS Accidents_Count
FROM people
GROUP BY people.age, people.age_label
ORDER BY Count(case_number) DESC;

-- Age groups with most accidents
SELECT people.age_label, Count (case_number) AS Accidents_Count
FROM people
GROUP BY people.age_label
ORDER BY Count(case_number) DESC;

-- Age and Age group with the most non-fatal accidents
SELECT people.age, people.age_label, doa_status, Count (case_number) AS Accidents_Count
FROM people
WHERE doa_status = 'No Fatality'
GROUP BY people.age, people.age_label, doa_status
ORDER BY Count(case_number) DESC;

-- Age and Age group with the most fatal accidents
SELECT people.age, people.age_label, doa_status, Count (case_number) AS Accidents_Count
FROM people
WHERE doa_status = 'Fatal'
GROUP BY people.age, people.age_label, doa_status
ORDER BY Count(case_number) DESC;

SELECT vehicle_manufacturer, Count (*)
FROM people
GROUP BY accidents.state
ORDER BY Count (*) DESC;