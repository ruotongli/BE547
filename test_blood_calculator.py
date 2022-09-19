import pytest
@pytest.mark.parametrize('input,expected',[(85,'Normal'),(50, 'Borderline low'),(35,'Low')])
def test_check_HDL(input,expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input)
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