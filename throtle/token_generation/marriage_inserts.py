"""
CREATE TABLE IF NOT EXISTS
reference.throtle_marriage_status
(marriage_status STRING, token STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

marriage_status token
M  TR_MS_M
S  TR_MS_S
...

LOAD DATA LOCAL INPATH '/tmp/throtle_marriage_status.tsv' INTO TABLE reference.throtle_marriage_status;
"""
with open('./throtle_marriage_status.tsv', 'w') as fh:
    for v in ('M', 'S'):
        fh.write("{0}\tTR_MS_{0}\n".format(v))
