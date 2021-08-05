#  pytest -v -s --html=Reports/test_ApproveRequisition.html --self-contained-html Testcases/test_ApproveRequisition.py --browser Firefox
#  pytest -v -s Testcases/test_ApproveRequisition.py --browser Firefox
#  pytest -v -s Testcases/test_ApproveRequisition.py --browser Chrome

from selenium.common.exceptions import NoSuchElementException
from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Approve_Requisition import ApproveRequisition
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Approve_Requisition:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=9)
    def test_Approve_Requisition_success(self,setup):

        """PREREQUIRMENTS"""

        ##Create new requisition
        #PREREQUIRMENTS.CREATE_REQUISITION(self,setup)

        """TESTCASE STARTS HERE"""
        #Login

        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click approve_Req
        self.cr = CreateRequisition(self.driver)  # classObject
        self.ar = ApproveRequisition(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        try:
         self.ar.click_Approve_Requisition()
        except:
            self.cr.Click_Requisition_Dropdown()
            self.ar.click_Approve_Requisition()
        RequisitionNumber=self.ar.get_table_data()
        self.ar.click_Approve_Req_Button()
        self.ar.click_Approve_Button()
        #Check the URL
        ExpectedURL="http://qa.coolmindsinc.com/plantrich-qa/#/home/requisitions/approve-requisition"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            try:
                RequisitionNumber_new = self.ar.get_table_data()
                if RequisitionNumber_new != RequisitionNumber:
                    self.driver.close()
                    assert True
                else:
                    # To take the Screenshote
                    PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                    assert False
            except NoSuchElementException:
                self.driver.close()
                assert True
            except:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False

class Test_002_Approve_Requisition:


    @pytest.mark.regression
    @pytest.mark.run(order=10)
    def test_Decline_Requisition(self, setup):

        """PREREQUIRMENTS"""

        ##Create new requisition
        PREREQUIRMENTS.CREATE_REQUISITION(self, setup)

        """TESTCASE STARTS HERE"""
        # Login
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.login()

        # Click approve_Req
        self.cr = CreateRequisition(self.driver)  # classObject
        self.ar = ApproveRequisition(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
        self.cr.Click_Requisition_Dropdown()
        try:
            self.ar.click_Approve_Requisition()
        except:
            self.cr.Click_Requisition_Dropdown()
            self.ar.click_Approve_Requisition()
        RequisitionNumber = self.ar.get_table_data()
        self.ar.click_Approve_Req_Button()
        self.ar.click_Decline_Button()
        # Check the URL
        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/requisitions/approve-requisition"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            try:
                RequisitionNumber_new = self.ar.get_table_data()
                if RequisitionNumber_new != RequisitionNumber:
                    self.driver.close()
                    assert True
                else:
                    # To take the Screenshote
                    PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                    assert False
            except NoSuchElementException:
                self.driver.close()
                assert True
            except:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False