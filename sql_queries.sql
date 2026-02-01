-- Query 1
-- Find the top 10 vehicles with the highest number of traffic stops
SELECT vehicle_number,
       COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY vehicle_number
ORDER BY total_stops DESC
LIMIT 10;

-- Query 2
-- Find the vehicles that were searched most frequently
SELECT vehicle_number,
       COUNT(*) AS search_count
FROM traffic_stops
WHERE search_conducted = 1
GROUP BY vehicle_number
ORDER BY search_count DESC
LIMIT 10;

-- Query 3
-- Identify which driver age group has the highest number of arrests
SELECT 
  CASE
    WHEN driver_age < 25 THEN 'Below 25'
    WHEN driver_age BETWEEN 25 AND 40 THEN '25 to 40'
    WHEN driver_age BETWEEN 41 AND 60 THEN '41 to 60'
    ELSE 'Above 60'
  END AS age_group,
  COUNT(*) AS arrest_count
FROM traffic_stops
WHERE is_arrested = 1
GROUP BY age_group
ORDER BY arrest_count DESC;

-- Query 4
-- Analyze gender distribution of drivers stopped in each country
SELECT country_name,
       driver_gender,
       COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY country_name, driver_gender
ORDER BY country_name;

-- Query 5
-- Find the time of day when traffic stops are most frequent
SELECT HOUR(stop_time) AS stop_hour,
       COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY stop_hour
ORDER BY total_stops DESC;







