#  pytest -v -s --html=Reports/test_CreateQuote.html --self-contained-html Testcases/test_CreateQuote.py --browser Firefox
#  pytest -v -s Testcases/test_CreateQuotes.py --browser Firefox
#  pytest -v -s Testcases/test_CreateQuotes.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from Prerequirments.Prerequirments import PREREQUIRMENTS
from PageObjects.Create_Quotes import CreateQuotes
from Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_CreateQuotes:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=11)
    def test_Create_Quote_success(self,setup):

        """PREREQUIRMENTS"""

        ##Create new requisition
        #PREREQUIRMENTS.CREATE_REQUISITION(self, setup)
        ##Approve Requisition
        #PREREQUIRMENTS.APPROVE_REQUISITION(self, setup)

        """TESTCASE STARTS HERE"""
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click createQuote
        self.cr = CreateRequisition(self.driver)  # classObject
        self.cq = CreateQuotes(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        self.cq.create_quote_click()
        RequisitionNumber=self.cq.get_latest_requisition_number()
        self.cq.click_action()
        self.cq.serch_vendor("Plantrich")
        self.cq.vendor_data_select()
        #add price
        self.cq.give_pricePROD1("20")
        self.cq.give_pricePROD2("30")
        #add note
        self.cq.give_note_PROD1("price added")
        self.cq.give_note_PROD2("PRICE ADDED")
        #submit
        self.cq.click_on_create_quote()

        ExpectedURL="http://qa.coolmindsinc.com/plantrich-qa/#/home/requisition-quotes/requisitions-quotes"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            RequisitionNumber_new = self.cq.get_latest_requisition_number()
            if RequisitionNumber_new == RequisitionNumber:
                self.driver.close()
                assert True
            else:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False

class Test_002_CreateQuotes:

    @pytest.mark.regression
    @pytest.mark.run(order=12)
    def test_Create_Quote_failure(self,setup):

        """PREREQUIRMENTS"""

        ##Create new requisition
        #PREREQUIRMENTS.CREATE_REQUISITION(self, setup)
        ##Approve Requisition
        #PREREQUIRMENTS.APPROVE_REQUISITION(self, setup)

        """TESTCASE STARTS HERE"""
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click approve_Req
        self.cr = CreateRequisition(self.driver)  # classObject
        self.cq = CreateQuotes(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        self.cq.create_quote_click()
        self.cq.click_action()

        #submit
        self.cq.click_on_create_quote()

        ##Check for popup msg
        text=self.cq.get_popup_msg()
        if 'Please select a vendor' in text:
            self.driver.close()
            assert True
        else:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False




