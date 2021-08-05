#  pytest -v -s --html=Reports/test_Pay_purchase_bill.html --self-contained-html Testcases/test_Pay_purchase_bill.py --browser Firefox
#  pytest -v -s Testcases/test_Pay_purchase_bill.py --browser Firefox
#  pytest -v -s Testcases/test_Pay_purchase_bill.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Create_PO import Create_PO
from PageObjects.Pay_Purchase_bill import Pay_Purchase_bill
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Pay_purchase_bill:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=30)
    def test_Pay_purchase_bill(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASE STARTS HERE"""
        self.driver = setup
        self.driver.get(BASEURL)
        # Classobjects
        self.lp = Login(self.driver)
        self.cr=CreateRequisition(self.driver)
        self.po=Create_PO(self.driver)
        self.pp=Pay_Purchase_bill(self.driver)

        #Login
        self.lp.login()
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.pp.Click_Pay_PB()
        self.pp.Search_PO("PURCHASE-")
        self.pp.Add_data("HDFC CASH ACCOUNT","Test")
        self.pp.Amount("1")
        self.pp.Click_Pay_Now()

        ExpectedURL="http://qa.coolmindsinc.com/plantrich-qa/#/home/purchaseOrder/list-purchase-order-payments"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False

