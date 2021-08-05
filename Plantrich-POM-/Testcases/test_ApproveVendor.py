#  pytest -v -s --html=Reports/test_ApproveVendor.html --self-contained-html Testcases/test_ApproveVendor.py --browser Firefox
#  pytest -v -s Testcases/test_ApproveVendor.py --browser Firefox
#  pytest -v -s Testcases/test_ApproveVendor.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from Prerequirments.Prerequirments import PREREQUIRMENTS
from PageObjects.Create_vendor import CreateVendor
from PageObjects.Approve_vendor import Approve_vendor
from Utilities.readproperties import ReadConfig
import pytest


BASEURL=ReadConfig.getBaseuRL()

class Test_001_prove_vendor:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=33)
    def test_Approve_Vendor_success(self,setup):
        """Pre requirments"""

        """Testcase Starts here"""
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)  # classObject
        self.cv = CreateVendor(self.driver)  # classObject
        self.av = Approve_vendor(self.driver)  # classObject
        self.lp.login()

        #Click ManageVendor
        try:
            self.cv.Click_ManageVendor()
        except:
            self.cr.Click_MenuIcon()
            self.cv.Click_ManageVendor()
        self.av.Click_view_vendor()
        self.av.Goto_last_page()
        self.av.Approve_last_vendor()
        self.av.Confirm_yes()
        self.av.Goto_last_page()
        code=self.av.check_approved()
        if code.startswith("VEN"):
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False

class Test_002_Approve_Vendor:


    @pytest.mark.regression
    @pytest.mark.run(order=34)
    def test_Declain_Vendor(self,setup):

        """Pre requirments """
        PREREQUIRMENTS.CREATE_VENDOR(self,setup)
        """Testcase Starts here"""
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)  # classObject
        self.cv = CreateVendor(self.driver)  # classObject
        self.av = Approve_vendor(self.driver)  # classObject
        self.lp.login()

        #Click createVendor
        try:
            self.cv.Click_ManageVendor()
        except:
            self.cr.Click_MenuIcon()
            self.cv.Click_ManageVendor()
        self.av.Click_view_vendor()
        self.av.Goto_last_page()
        self.av.Declain_last_vendor()
        self.av.Confirm_yes_declain()
        self.av.Goto_last_page()
        Length=self.av.check_Declined()
        if Length==6:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        elif Length == 5:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False


