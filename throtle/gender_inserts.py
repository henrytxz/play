"""
CREATE TABLE IF NOT EXISTS
reference.throtle_gender
(gender STRING, token STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

gender  token
M       TR_G_M
F       TR_G_F
...

LOAD DATA LOCAL INPATH '/tmp/throtle_gender.tsv' INTO TABLE reference.throtle_gender;
"""
with open('./throtle_gender.tsv', 'w') as fh:
    for g in ('M', 'F'):
        fh.write("{0}\tTR_G_{0}\n".format(g))
