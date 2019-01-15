"""
Below are all the possible values for each attribute:
Age: 18-99
Gender: M or F
Marriage Status: M or S
Education: 1,2,3, or 4
Household Income: A,B,C,D,E,F,G,H,I,J,K,L,M,N,O
Race: A1,A2,A3,A4,A5,B1,B2,H1,H2,I1,M1,M2,W1,W2,W3,W4,W5,W6,W7,W8
Home Price: Blank or 1-999

this script generates all segments
so I can publish them to get an OK from stakeholders

idea:
append TR/
use / as a separator

G for Gender
MS for Marriage Status
E for Education
HI for Household Income
R for Race
A for Age
HP for Home Price
"""

prefix = 'TR/'
slash = '/'

for v in ('Male', 'Female'):
    print prefix + 'Gender' + slash + v

for v in ('Married', 'Single'):
    print prefix + 'Marriage Status' + slash + v

for v in ('High School',
          'Some College',
          'Completed College',
          'Graduated School'):
    print prefix + 'Education' + slash + v

for v in ('Under $10K',
        '10-19,999',
        '20-29,999',
        '30-39,999',
        '40-49,999',
        '50-59,999',
        '60-69,999',
        '70-79,999',
        '80-89,999',
        '90-99,999',
        '100-149,999',
        '150-174,999',
        '175-199,999',
        '200-249,999',
        '250K+'):
    print prefix + 'Household Income' + slash + v

for v in ('Asian - Unknown',
        'Asian - Chinese',
        'Asian - Indian',
        'Asian - Japanese',
        'Asian - Oriental',
        'African American - African Origin',
        'African American - American Origin',
        'Hispanic - Hispanic Origin',
        'Hispanic - Portuguese Origin',
        'American Indian',
        'Middle Eastern - Arabs',
        'Middle Eastern - Egyptian',
        'Caucasian - English',
        'Caucasian - European',
        'Caucasian - White Non-American',
        'Caucasian - Unknown',
        'Caucasian - Eastern European',
        'Caucasian - Jewish',
        'Caucasian - Greek',
        'Caucasian - Dutch'):
    print prefix + 'Race' + slash + v

for v in range(18, 100):
    print prefix + 'Age' + slash + str(v)

for v in range(1, 1000):
    print prefix + 'Home Price' + slash + str(v * 1000)

for attribute in ('Gender',
                  'Marriage Status',
                  'Education',
                  'Household Income',
                  'Race',
                  'Age',
                  'Home Price'):
    print prefix + attribute + slash + 'Unknown'
