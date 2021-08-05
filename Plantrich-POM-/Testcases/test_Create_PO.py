#  pytest -v -s --html=Reports/test_Create_PO.html --self-contained-html Testcases/test_Create_PO.py --browser Firefox
#  pytest -v -s Testcases/test_Create_PO.py --browser Firefox
#  pytest -v -s Testcases/test_Create_PO.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_PO import Create_PO
from PageObjects.Create_Requisition import CreateRequisition
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Create_PO:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=15)
    def test_Create_PO_success(self,setup):

        """PREREQUIRMENTS"""
        ##Create Quote
        #PREREQUIRMENTS.CREATE_QUOTE(self, setup)
        ##Approve Quote
        #PREREQUIRMENTS.APPROVE_QUOTE(self, setup)

        """TESTCASE STARTS HERE"""
        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.po=Create_PO(self.driver)

        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.po.Click_Create_PO()
        self.po.Click_Search_requisition("REQ-")
        self.po.Click_Select_requisition()
        self.po.Select_MOT("Road way")
        self.po.Enter_delivary_location("ware1")
        self.po.Payment_terms("Test purpose")
        self.po.Select_ETA()
        self.po.Select_IGST("18")
        self.po.Select_Freight("Inclusive")
        self.po.Create_PO_submit()

        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/purchaseOrder/table-purchase-order"

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            #To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False


class Test_002_Create_PO:


    @pytest.mark.regression
    @pytest.mark.run(order=16)
    def test_Create_PO_fail(self,setup):

        """PREREQUIRMENTS"""
        ##Create Quote
        #PREREQUIRMENTS.CREATE_QUOTE(self, setup)
        ##Approve Quote
        #PREREQUIRMENTS.APPROVE_QUOTE(self, setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.po=Create_PO(self.driver)

        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.po.Click_Create_PO()
        self.po.Click_Search_requisition("REQ-")
        self.po.Click_Select_requisition()
        self.po.Create_PO_submit()
        ##Check for popup msg
        text = self.po.get_popup_msg()
        if 'Please select Mode of Transportation' in text:
            self.driver.close()
            assert True
        else:
            ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/purchaseOrder/table-purchase-order"
            try:
                WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
            except:
                self.driver.close()
                assert True


