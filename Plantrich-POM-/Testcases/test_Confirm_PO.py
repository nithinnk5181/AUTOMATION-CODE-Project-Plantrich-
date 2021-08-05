#  pytest -v -s --html=Reports/test_Confirm_PO.html --self-contained-html Testcases/test_Confirm_PO.py --browser Firefox
#  pytest -v -s Testcases/test_Confirm_PO.py --browser Firefox
#  pytest -v -s Testcases/test_Confirm_PO.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Create_PO import Create_PO
from PageObjects.Confirm_PO import Confirm_PO
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Confirm_PO:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=17)
    def test_Confirm_PO_Approve(self,setup):

        """PREREQUIRMENTS"""
        ##CreatePO
        #PREREQUIRMENTS.CREATE_PO(self,setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.po=Create_PO(self.driver)
        self.cp=Confirm_PO(self.driver)

        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.cp.Click_confirm_PO_item()
        lattest_POnum=self.cp.Get_lattest_PO_number()
        self.cp.Click_Action_lattest_PO()
        self.cp.Click_Approve_button()
        self.cp.Click_Approve_Confirm_yes()
        updated_PO_num=self.cp.Get_lattest_PO_number()
        if updated_PO_num==lattest_POnum:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        else:
            assert True
            self.driver.close()


class Test_002_Confirm_PO:

    @pytest.mark.regression
    @pytest.mark.run(order=18)
    def test_Confirm_PO_Declain(self,setup):

        """PREREQUIRMENTS"""
        ##CreatePO
        PREREQUIRMENTS.CREATE_PO(self,setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.po=Create_PO(self.driver)
        self.cp=Confirm_PO(self.driver)

        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.cp.Click_confirm_PO_item()
        lattest_POnum=self.cp.Get_lattest_PO_number()
        self.cp.Click_Action_lattest_PO()
        self.cp.Click_Declain_button()
        self.cp.Click_Declain_Confirm_yes()
        updated_PO_num=self.cp.Get_lattest_PO_number()
        if updated_PO_num==lattest_POnum:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        else:
            assert True
            self.driver.close()

