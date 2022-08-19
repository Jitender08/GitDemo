import pytest


@pytest.mark.smoke

def test_firstprogram(setup):
    print("hello")

@pytest.mark.xfail
def test_greetcreditcard():
    print("hello")

def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])