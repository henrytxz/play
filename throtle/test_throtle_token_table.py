import pytest
from throtle.throtle_token_table import age_bracket, build_attribute_value_to_token_map


def test_age_bracket():
    """
    brackets = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65+']
    thresholds = [25, 30, 35, 40, 45, 50, 55, 60, 65, 100]
    divide by 5 => [5, 6, 7, 8, 9, 10, 11, 12, 13, 20]

    brackets = {
        3:  '18-24',
        4:  '18-24',
        5:  '25-29',
        6:  '30-34',
        7:  '35-39',
        8:  '40-44',
        9:  '45-49',
        10: '50-54',
        11: '55-59',
        12: '60-64',
        13: '65+'
    }
    """
    assert age_bracket(18) == '18-24'
    assert age_bracket(20) == '18-24'
    assert age_bracket(24) == '18-24'
    assert age_bracket(25) == '25-29'
    assert age_bracket(30) == '30-34'
    assert age_bracket(35) == '35-39'
    assert age_bracket(40) == '40-44'
    assert age_bracket(45) == '45-49'
    assert age_bracket(50) == '50-54'
    assert age_bracket(55) == '55-59'
    assert age_bracket(60) == '60-64'
    assert age_bracket(65) == '65-plus'
    assert age_bracket(99) == '65-plus'
    with pytest.raises(AssertionError):
        age_bracket(17)
    with pytest.raises(AssertionError):
        age_bracket(100)

def test_g():
    d = build_attribute_value_to_token_map()
    assert d['G_M'] == 'TR_G_M'

def test_ms():
    d = build_attribute_value_to_token_map()
    assert d['MS_M'] == 'TR_MS_M'

def test_e():
    d = build_attribute_value_to_token_map()
    assert d['E_1'] == 'TR_E_1'

def test_hi():
    d = build_attribute_value_to_token_map()
    assert d['HI_A'] == 'TR_HI_$0-50k'
    assert d['HI_K'] == 'TR_HI_$100-150k'
    assert d['HI_O'] == 'TR_HI_$150k+'

def test_r():
    d = build_attribute_value_to_token_map()
    assert d['R_A1'] == 'TR_R_0'
    assert d['R_W8'] == 'TR_R_19'

def test_a():
    d = build_attribute_value_to_token_map()
    assert d['A_18'] == 'TR_A_18-24'

# def test_hp():
#     d = build_attribute_value_to_token_map()
#     assert d['HP_'] == ''
