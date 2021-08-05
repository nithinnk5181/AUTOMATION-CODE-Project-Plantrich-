#  pytest -v -s --html=Reports/test_Generate_purchase_bill.html --self-contained-html Testcases/test_Generate_purchase_bill.py --browser Firefox
#  pytest -v -s Testcases/test_Generate_purchase_bill.py --browser Firefox
#  pytest -v -s Testcases/test_Generate_purchase_bill.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Create_PO import Create_PO
from PageObjects.Generate_purchase_bill import Generate_purchase_bill
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Generate_purchase_bill:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=29)
    def test_Generate_purchase_bill(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASE STARTS HERE"""
        self.driver = setup
        self.driver.get(BASEURL)
        # Classobjects
        self.lp = Login(self.driver)
        self.cr=CreateRequisition(self.driver)
        self.po=Create_PO(self.driver)
        self.gp=Generate_purchase_bill(self.driver)

        #Login
        self.lp.login()
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.gp.Click_on_Generate_PB()
        self.gp.Click_on_Action()
        self.gp.Click_on_GenerateButton()
        ExpectedURL="http://qa.coolmindsinc.com/plantrich-qa/#/home/purchaseOrder/confirm-purchase-order"

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))
            assert True
            self.driver.close()

        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False


