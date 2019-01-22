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

A: 18-24, 29, 34, 39, 44, 49, 54, 59, 64, 65+
"""

prefix = 'TR/'
slash = '/'

g = 'G'
ms = 'MS'
e = 'E'
hi = 'HI'
r = 'R'
a = 'A'
hp = 'HP'

token_prefix = 'TR_'
underscore = '_'
comma = ','

gender_values = ('Male', 'Female')
for v in gender_values:
    print '{0},{1}'.format(prefix + g + slash + v, token_prefix + g + underscore + str(gender_values.index(v)))

ms_values = ('Married', 'Single')
for v in ms_values:
    print '{0},{1}'.format(prefix + ms + slash + v, token_prefix + ms + underscore + str(ms_values.index(v)))

education_values = ('High School',
                  'Some College',
                  'Completed College',
                  'Graduated School')
for v in education_values:
    print '{0},{1}'.format(prefix + e + slash + v, token_prefix + e + underscore + str(education_values.index(v)))

hi_values = ('Under $10K',
        '10-19999',
        '20-29999',
        '30-39999',
        '40-49999',
        '50-59999',
        '60-69999',
        '70-79999',
        '80-89999',
        '90-99999',
        '100-149999',
        '150-174999',
        '175-199999',
        '200-249999',
        '250K+')
for v in hi_values:
    print '{0},{1}'.format(prefix + hi + slash + v, token_prefix + hi + underscore + str(hi_values.index(v)))

r_values = ('Asian - Unknown',
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
        'Caucasian - Dutch')
for v in r_values:
    print '{0},{1}'.format(prefix + r + slash + v, token_prefix + r + underscore + str(r_values.index(v)))

a_values = range(18, 100)
for v in a_values:
    print '{0},{1}'.format(prefix + a + slash + str(v), token_prefix + a + underscore + str(v))

hp_values = range(1, 1000)
for v in hp_values:
    print '{0},{1}'.format(prefix + hp + slash + str(v * 1000), token_prefix + hp + underscore + str(v))

# for attribute in (g, ms, e, hi, r, a, hp):
#     print prefix + attribute + slash + 'Unknown'
