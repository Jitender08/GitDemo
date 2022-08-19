import pytest

@pytest.mark.skip
def test_firstprogram():
    msg ="hello"
    assert msg =="hi, test failed"

@pytest.mark.smoke
def test_secondprogramcreditcard():
    a = 4
    b = 6
    assert a+2 == b
