-- displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
