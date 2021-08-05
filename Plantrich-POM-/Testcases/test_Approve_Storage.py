#  pytest -v -s --html=Reports/test_Approve_Storage.html --self-contained-html Testcases/test_Approve_Storage.py --browser Firefox
#  pytest -v -s Testcases/test_Approve_Storage.py --browser Firefox
#  pytest -v -s Testcases/test_Approve_Storage.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Approve_Storage import Approve_storage
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest
from selenium.common.exceptions import TimeoutException


BASEURL=ReadConfig.getBaseuRL()

class Test_001_Appprove_Material_Storage:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=26)
    def test_Approve_Material_Storage(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.As = Approve_storage(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.As.click_Approve_storage()
        except:
            self.cr.Click_MenuIcon()
            self.As.click_Approve_storage()
        lattestID=self.As.Get_lattest_id()
        self.As.Click_action()
        self.As.Approve()
        try:
            UpdatedID = self.As.Get_lattest_id()
            if UpdatedID==lattestID:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
            else:
                self.driver.close()
                assert True
        except TimeoutException:
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False



class Test_002_Appprove_Material_Storage:


    @pytest.mark.regression
    @pytest.mark.run(order=27)
    def test_Declain_Material_Storage(self,setup):

        """PREREQUIRMENTS"""
        PREREQUIRMENTS.CREATE_MATERIAL_INWARD(self, setup)
        PREREQUIRMENTS.CREATE_MATERIAL_QC(self,setup)
        PREREQUIRMENTS.CREATE_MATERIAL_STORAGE(self,setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.As = Approve_storage(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.As.click_Approve_storage()
        except:
            self.cr.Click_MenuIcon()
            self.As.click_Approve_storage()
        lattestID=self.As.Get_lattest_id()
        self.As.Click_action()
        self.As.Declain()

        try:
            UpdatedID = self.As.Get_lattest_id()
            if UpdatedID == lattestID:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
            else:
                self.driver.close()
                assert True
        except TimeoutException:
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False