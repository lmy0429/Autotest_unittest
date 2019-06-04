from testbase.api import Testbase
from data import search
from testbase.__init__ import SAE


class Testcase(SAE):
    def test_search(self):
        driver = Testbase(self.driver)
        driver.send_key(search.searchinput, search.search)
        driver.click(search.submit)
        driver.wait(search.assert1)
        a = driver.textvalue(search.assert1)
        print(a)
        b = driver.attributevalue(search.assert2, 'tpl')
        print(b)
