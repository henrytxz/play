"""
CREATE TABLE IF NOT EXISTS
reference.throtle_education
(education TINYINT, token STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

education token
1  TR_E_1
2  TR_E_2
...

LOAD DATA LOCAL INPATH '/tmp/throtle_education.tsv' INTO TABLE reference.throtle_education;
"""
with open('./throtle_education.tsv', 'w') as fh:
    for v in range(1, 5):
        fh.write("{0}\tTR_E_{0}\n".format(v))
