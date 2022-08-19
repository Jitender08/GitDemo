import pytest
@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ("Jitender", "Gupta", "rahulshettyacademy.com")


@pytest.fixture(params=(("chrome", "jitender"),("Firefox", "Gupta"), ("IE", "mine")))
def crossbrowser(request):
    return request.param
