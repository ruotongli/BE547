import pytest
@pytest.mark.parametrize('input,expected',[(85,'Normal'),(50, 'Borderline low'),(35,'Low')])
def test_check_HDL(input,expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input)
    assert answer == expected
    
@pytest.mark.parametrize('input,expected',
    [(120,'Normal'),
    (140, 'Borderline high'),
    (170,'High'),
    (200,'Very high')])
def test_check_LDL(input,expected):
    from blood_calculator import check_LDL
    answer = check_LDL(input)
    assert answer == expected

@pytest.mark.parametrize('input,expected',
    [(180,'Normal'),
    (220, 'Borderline high'),
    (250,'High')])
def test_check_total(input,expected):
    from blood_calculator import check_total
    answer = check_total(input)
    assert answer == expected
"""
def test_check_HDL_Borderlinelow(input,expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input)
    expected = 'Borderline low'
    assert answer == expected

def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer = check_HDL(35)
    expected = 'Low'
    assert answer == expected
"""