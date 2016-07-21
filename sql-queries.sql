-- Main Table creation
CREATE TABLE atom_wifi_data (
  mac_addr VARCHAR(1000),
  first_seen TIMESTAMP,
  last_seen TIMESTAMP,
  insertion_time TIMESTAMP,
  device_type VARCHAR(1000)
)
;
-- Alter table to add device type (wasn't in the original creation query)
ALTER TABLE atom_wifi_data
    add column device_type VARCHAR(1000)
default NULL
;
-- Get average time a user stays in the store
select avg(datediff(minute, first_seen, last_seen))
from atom_wifi_data
;
-- Get the most popular hours
select to_char(first_seen, 'HH24') as hour, count(to_char(first_seen, 'HH24')) from atom_wifi_data
group by to_char(first_seen, 'HH24')
order by hour
;
select *
from (
  select device_type, count(device_type) as counter, rank() over (order by count(device_type) desc) as counter_rank
  from atom_wifi_data
  where device_type is not null
  group by device_type
)
where counter_rank <= 10
order by counter_rank asc
