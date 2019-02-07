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

def age_bracket(age):
    # age: int
    assert age >= 18
    assert age < 100
    brackets = {
        3 : '18-24',
        4 : '18-24',
        5 : '25-29',
        6 : '30-34',
        7 : '35-39',
        8 : '40-44',
        9 : '45-49',
       10 : '50-54',
       11 : '55-59',
       12 : '60-64',
       13 : '65-plus',
       14 : '65-plus',
       15 : '65-plus',
       16 : '65-plus',
       17 : '65-plus',
       18 : '65-plus',
       19 : '65-plus'
    }
    return brackets[age//5]


token_prefix = 'TR_'
underscore = '_'
comma = ','

def build_attribute_value_to_token_map():
    d = {}

    g = 'G'
    ms = 'MS'
    e = 'E'
    hi = 'HI'
    r = 'R'
    a = 'A'

    gender_values = ('M', 'F')
    for v in gender_values:
        d.update({g + underscore + v : token_prefix + g + underscore + v})

    ms_values = ('M', 'S')
    for v in ms_values:
        d.update({ms + underscore + v : token_prefix + ms + underscore + v})

    education_values = range(1, 5)
    for v in education_values:
        d.update({e + underscore + str(v) : token_prefix + e + underscore + str(v)})

    """
    $0-50k
    $50-100k
    $100-150k
    $150k+

    Token       ADVID   Name
    AA_30206	5141	PP/Income Bracket/$0-50k	LiveRamp Token
    AA_30207	5141	PP/Income Bracket/$50-100k	LiveRamp Token
    AA_30208	5141	PP/Income Bracket/$100-150k	LiveRamp Token
    AA_30209	5141	PP/Income Bracket/$150k+	LiveRamp Token
    """
    hi_map = {'A' : '$0-50k',
              'B' : '$0-50k',
              'C' : '$0-50k',
              'D' : '$0-50k',
              'E' : '$0-50k',
              'F' : '$50-100k',
              'G' : '$50-100k',
              'H' : '$50-100k',
              'I' : '$50-100k',
              'J' : '$50-100k',
              'K' : '$100-150k',
              'L' : '$150k+',
              'M' : '$150k+',
              'N' : '$150k+',
              'O' : '$150k+'}
    hi_values = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O'.split(',')
    for v in hi_values:
        d.update({hi + underscore + v : token_prefix + hi + underscore + hi_map[v]})

    r_values = 'A1,A2,A3,A4,A5,B1,B2,H1,H2,I1,M1,M2,W1,W2,W3,W4,W5,W6,W7,W8'.split(',')
    for v in r_values:
        d.update({r + underscore + v : token_prefix + r + underscore + str(r_values.index(v))})

    """
    brackets = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65+']
    thresholds = [25, 30, 35, 40, 45, 50, 55, 60, 65, 100]
    divide by 5 => [5, 6, 7, 8, 9, 10, 11, 12, 13, 20]
    """
    a_values = range(18, 100)
    for v in a_values:
        d.update({a + underscore + str(v) : token_prefix + a + underscore + age_bracket(v)})

    hp_bracket(d)
    return d


def hp_bracket(d):
    """
    hp: Home purchase price expressed in thousands. Range : 0-999

    10k
    50
    100
    120
    150
    200
    300
    400
    500
    750
    1 mil
    """
    hp = 'HP'
    hp_values = range(1, 1000)
    brackets = ['0-10k',
                '10-50k',
                '50-100k',
                '100-120k',
                '120-150k',
                '150-200k',
                '200-300k',
                '300-400k',
                '400-500k',
                '500-750k',
                '750-999k',
                '999k-plus']
    bracket = brackets.pop(0)
    thresholds = [10, 50, 100, 120, 150, 200, 300, 400, 500, 750, 999, 1000]
    threshold = thresholds.pop(0)
    for v in hp_values:
        if v == threshold:
            bracket = brackets.pop(0)
            threshold = thresholds.pop(0)
        d[hp + underscore + str(v) + 'k'] = token_prefix + hp + underscore + bracket


if __name__ == '__main__':
    for k, v in build_attribute_value_to_token_map().items():
        print(f'{k}, {v}')

    # for b in ['$0-10k',
    #             '$10-50k',
    #             '$50-100k',
    #             '$100-120k',
    #             '$120-150k',
    #             '$150-200k',
    #             '$200-300k',
    #             '$300-400k',
    #             '$400-500k',
    #             '$500-750k',
    #             '$750-999k',
    #             '$999k+']:
    #     print(f'TR/HP/{b}', f'TR_HP_{b}')

