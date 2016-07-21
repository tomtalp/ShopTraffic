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
select to_char(first_seen, 'HH24'), count(to_char(first_seen, 'HH24')) from atom_wifi_data
group by to_char(first_seen, 'HH24')
;
