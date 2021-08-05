#  pytest -v -s --html=Reports/test_Add_product.html --self-contained-html Testcases/test_Add_product.py --browser Firefox
#  pytest -v -s Testcases/test_Add_product.py --browser Firefox
#  pytest -v -s Testcases/test_Add_product.py --browser Chrome

from Utilities.readproperties import ReadConfig
from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Add_Products import Add_product
from Prerequirments.Prerequirments import PREREQUIRMENTS
import pytest

class Test_001_Add_Product:

    BaseURL=ReadConfig.getBaseuRL()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=35)
    def test_AddProduct_success(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASESTARTSHERE"""
        #SETUP
        self.driver=setup
        self.driver.get(self.BaseURL)

        #ClassObjects
        self.lp=Login(self.driver)
        self.cr = CreateRequisition(self.driver)
        self.ap = Add_product(self.driver)

        #Login
        self.lp.login()

        try:
            self.ap.Click_on_Product()
        except:
            self.cr.Click_MenuIcon()
            self.ap.Click_on_Product()
        self.ap.Goto_last_page()
        lattest_num=self.ap.Get_lattest_added_name()
        self.ap.Click_Add_product()
        self.ap.Add_Data()
        self.ap.Add_Attributes("TEST","10")
        self.ap.Click_Submit()
        self.ap.Goto_last_page()
        updated_num=self.ap.Get_lattest_added_name()

        if lattest_num==updated_num:
            # Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        else:
            assert True
            self.driver.close()


class Test_002_Add_Product:

    BaseURL=ReadConfig.getBaseuRL()

    @pytest.mark.regression
    @pytest.mark.run(order=36)
    def test_AddProduct_fail(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASESTARTSHERE"""
        #SETUP
        self.driver=setup
        self.driver.get(self.BaseURL)

        #ClassObjects
        self.lp=Login(self.driver)
        self.cr = CreateRequisition(self.driver)
        self.ap = Add_product(self.driver)

        #Login
        self.lp.login()

        try:
            self.ap.Click_on_Product()
        except:
            self.cr.Click_MenuIcon()
            self.ap.Click_on_Product()
        self.ap.Click_Add_product()
        self.ap.Click_Submit()
        try:
            self.ap.Goto_last_page()
            updated_num=self.ap.Get_lattest_added_name()

            # Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            assert True
            self.driver.close()
















