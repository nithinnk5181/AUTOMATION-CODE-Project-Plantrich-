#  pytest -v -s --html=Reports/test_Add_Storage_stock.html --self-contained-html Testcases/test_Add_Storage_stock.py --browser Firefox
#  pytest -v -s Testcases/test_Add_Storage_stock.py --browser Firefox
#  pytest -v -s Testcases/test_Add_Storage_stock.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Add_Storage_Stock import Add_stock
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Add_storage_stock:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=28)
    def test_Add_storage_stock(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.As = Add_stock(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.As.Click_add_to_stock()
        except:
            self.cr.Click_MenuIcon()
            self.As.Click_add_to_stock()
        LattestID=self.As.Get_lattest_id()
        self.As.Click_Action_lattest()
        self.As.Click_add_to_stock_button()
        UpdatedID = self.As.Get_lattest_id()
        if UpdatedID==LattestID:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        else:
            self.driver.close()
            assert True




