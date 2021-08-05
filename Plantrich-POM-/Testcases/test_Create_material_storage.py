#  pytest -v -s --html=Reports/test_material_storage.html --self-contained-html Testcases/test_Create_material_storage.py --browser Firefox
#  pytest -v -s Testcases/test_Create_material_storage.py --browser Firefox
#  pytest -v -s Testcases/test_Create_material_storage.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Material_storage import Material_Storage
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Create_Material_Storage:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=23)
    def test_Create_Material_Storage(self,setup):

        """PREREQUIRMENTS"""
        #PREREQUIRMENTS.CREATE_MATERIAL_INWARD(self,setup)
        #PREREQUIRMENTS.CREATE_MATERIAL_QC(self, setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.ms = Material_Storage(self.driver)


        # Login
        self.lp.login()

        #Create_material Storage
        try:
            self.ms.Click_on_Material_Storage()
        except:
            self.cr.Click_MenuIcon()
            self.ms.Click_on_Material_Storage()
        self.ms.Click_Create_material_storage()
        self.ms.Select_lattest_material_inw_num("MIR-")
        self.ms.Select_Product1()
        self.ms.Add_data("TEST","100")
        self.ms.Submit()
        self.ms.Select_Product2()
        self.ms.Add_data("test","100")
        self.ms.Submit()

        self.ms.FinalSubmit()

        ExpectedURL="http://qa.coolmindsinc.com/plantrich-qa/#/home/material-storage/table-material-storage"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            #To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False


class Test_002_Create_Material_Storage:


    @pytest.mark.regression
    @pytest.mark.run(order=24)
    def test_Create_Material_Storage_fail(self,setup):

        """PREREQUIRMENTS"""
        PREREQUIRMENTS.CREATE_MATERIAL_INWARD(self,setup)
        PREREQUIRMENTS.CREATE_MATERIAL_QC(self, setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.ms = Material_Storage(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.ms.Click_on_Material_Storage()
        except:
            self.cr.Click_MenuIcon()
            self.ms.Click_on_Material_Storage()
        self.ms.Select_lattest_material_inw_num("MIR-")
        self.ms.Select_Product1()
        self.ms.Submit()
        try:
            self.ms.Select_Product2()
            self.ms.Submit()
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            self.driver.close()
            assert True


class Test_003_Create_Material_Storage:

    @pytest.mark.regression
    @pytest.mark.run(order=25)
    def test_Create_Material_Storage_fail2(self,setup):

        """PREREQUIRMENTS"""
        #PREREQUIRMENTS.CREATE_MATERIAL_INWARD(self,setup)
        #PREREQUIRMENTS.CREATE_MATERIAL_QC(self, setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.ms = Material_Storage(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.ms.Click_on_Material_Storage()
        except:
            self.cr.Click_MenuIcon()
            self.ms.Click_on_Material_Storage()
        self.ms.Select_lattest_material_inw_num("MIR-")
        self.ms.Select_Product1()
        self.ms.Add_data("TEST","100")
        self.ms.Submit()

        try:
            self.ms.FinalSubmit()
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            self.driver.close()
            assert True



