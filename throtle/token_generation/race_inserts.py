"""
CREATE TABLE IF NOT EXISTS
reference.throtle_race
(race STRING, token STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

race token

...

LOAD DATA LOCAL INPATH '/tmp/throtle_race.tsv' INTO TABLE reference.throtle_gender;
"""
with open('./throtle_race.tsv', 'w') as fh:
    for g in ('M', 'F'):
        fh.write("{0}\tTR_G_{0}\n".format(g))
