#  pytest -v -s --html=Reports/test_Approve_Quote.html --self-contained-html Testcases/test_Approve_Quote.py --browser Firefox
#  pytest -v -s Testcases/test_Approve_Quote.py --browser Firefox
#  pytest -v -s Testcases/test_Approve_Quote.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from Prerequirments.Prerequirments import PREREQUIRMENTS
from PageObjects.Approve_Quote import Approve_quote
from Utilities.readproperties import ReadConfig
import datetime
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Approve_Quote:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=13)
    def test_Approve_Quote(self,setup):

        """PREREQUIRMENTS"""

        ##Create Quote
        #PREREQUIRMENTS.CREATE_QUOTE(self, setup)

        """TESTCASE STARTS HERE"""
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click Approve_Quote
        self.cr = CreateRequisition(self.driver)  # classObject
        self.aq = Approve_quote(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        self.aq.click_view_quote()
        self.aq.Goto_Approve_quote_page()
        self.aq.Click_Approve_quote()

        #checking the quote is approved or not
        try:
            self.aq.Click_Approve_quote()
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            assert True
            self.driver.close()



class Test_002_Approve_Quote:


    @pytest.mark.regression
    @pytest.mark.run(order=14)
    def test_Decline_Quote(self,setup):

        """PREREQUIRMENTS"""

        ##Create Quote
        PREREQUIRMENTS.CREATE_QUOTE(self, setup)

        """TESTCASE STARTS HERE"""
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click Approve_Quote
        self.cr = CreateRequisition(self.driver)  # classObject
        self.aq = Approve_quote(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        self.aq.click_view_quote()
        self.aq.Goto_Approve_quote_page()
        self.aq.Click_Declain_quote()

        # checking the quote is approved or not
        try:
            self.aq.Click_Declain_quote()
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            assert True
            self.driver.close()
