
SELECT hour, COUNT(DISTINCT date_ip) as unique_ip_count
FROM logs
GROUP BY hour



select YEAR(date_time) as Year, MONTHNAME(date_time) as Month, count(distinct date_ip) as unique_ip_count
from logs
group by 1, 2


select YEAR(date_time) as Year, MONTHNAME(date_time) as Month, DAY(date_time) as Day, hour, count(distinct ip) as unique_ip_count
from logs
group by 1, 2, 3, 4


-- Timeseries
SELECT
$__timeGroupAlias(time, '1h'),
count(distinct date_ip) as value
FROM logs
GROUP BY 1
ORDER BY 1