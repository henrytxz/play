"""
Age: 18-99

A: 18-24, 29, 34, 39, 44, 49, 54, 59, 64, 65+

CREATE TABLE IF NOT EXISTS
reference.throtle_age_token_mapping
(age TINYINT, token STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

age token
18  TR_A_18_24
25  TR_A_25_29
...

INSERT INTO reference.throtle_age_token_mapping VALUES (18, 'TR_A_18_24');

LOAD DATA LOCAL INPATH '/tmp/throtle_age_token_mapping.tsv' INTO TABLE reference.throtle_age_token_mapping;
"""
brackets = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65+']
bracket = brackets.pop(0)
thresholds = [25, 30, 35, 40, 45, 50, 55, 60, 65, 100]
# divide by 5 => [5, 6, 7, 8, 9, 10, 11, 12, 13, 20]
threshold = thresholds.pop(0)
# print bracket, threshold

with open('./throtle_age.tsv', 'w') as fh:
    for a in range(18, 100):
        if a == threshold:
            bracket = brackets.pop(0)
            threshold = thresholds.pop(0)
        # print "INSERT INTO reference.throtle_age_token_mapping VALUES ({0}, 'TR_A_{1}');".format(a, bracket)
        fh.write("{0}\tTR_A_{1}\n".format(a, bracket))
        # fh.write("TR_A_{0}\n".format(bracket))