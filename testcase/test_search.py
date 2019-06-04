from testbase.api import Testbase
from data import nokia_search
from testbase.__init__ import SAE
import ddt
from testbase.assistAPI import excelreader
from time import sleep


@ddt.ddt
class Testcase(SAE):
    @ddt.data(*(excelreader('sku (3).xlsx', 'product')))
    @ddt.unpack
    def test_search(self, searchtext, result):
        driver = Testbase(self.driver)
        driver.openurl(nokia_search.URL)
        self.driver.implicitly_wait(10)
        driver.wait(nokia_search.searchinput)
        driver.send_key(nokia_search.searchinput, searchtext)
        driver.click(nokia_search.submit)
        self.assertNotEqual(driver.assertelementdisplayed(nokia_search.noresult), result)
