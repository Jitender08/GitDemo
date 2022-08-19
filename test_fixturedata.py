import pytest

from baseclass import BaseClass


@pytest.mark.usefixtures("dataLoad")

class TestExample2(BaseClass):

    def test_editprofile(self, dataLoad):
        log = self.test_loggingDemo()
        log.critical(dataLoad[0])
        log.info(dataLoad[2])

