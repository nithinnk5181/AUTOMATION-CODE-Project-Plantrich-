#  pytest -v -s --html=Reports/test_Approve_Product.html --self-contained-html Testcases/test_Approve_Product.py --browser Firefox
#  pytest -v -s Testcases/test_Approve_Product.py --browser Firefox
#  pytest -v -s Testcases/test_Approve_Product.py --browser Chrome

from Utilities.readproperties import ReadConfig
from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Approve_product import Approve_product
from Prerequirments.Prerequirments import PREREQUIRMENTS
import pytest

class Test_001_Approve_Product:

    BaseURL=ReadConfig.getBaseuRL()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=37)
    def test_Approve_Product(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASESTARTSHERE"""
        #SETUP
        self.driver=setup
        self.driver.get(self.BaseURL)

        #ClassObjects
        self.lp=Login(self.driver)
        self.cr = CreateRequisition(self.driver)
        self.aap = Approve_product(self.driver)

        #Login
        self.lp.login()

        try:
            self.aap.Click_Catalog_Menuitem()
        except:
            self.cr.Click_MenuIcon()
            self.aap.Click_Catalog_Menuitem()
        self.aap.Click_Approve_Menuitem()
        self.aap.Goto_last_page()
        lattest_ID=self.aap.Get_lattest_num()
        self.aap.Click_Action_on_lattest()
        self.aap.Click_Approve_button()
        self.aap.Goto_last_page()
        updated_ID = self.aap.Get_lattest_num()

        if updated_ID==lattest_ID:
            # Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        else:
            assert True
            self.driver.close()


