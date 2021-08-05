#  pytest -v -s --html=Reports/test_CreateRequisition_report.html --self-contained-html Testcases/test_CreateRequisition.py --browser Firefox
#  pytest -v -s Testcases/test_CreateRequisition.py --browser Firefox
#  pytest -v -s Testcases/test_CreateRequisition.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

BASEURL=ReadConfig.getBaseuRL()
class Test_001_CreateRequisition:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=6)
    def test_CreateReq_Possitive(self,setup):
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click Create Req
        self.cr = CreateRequisition(self.driver)#classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        try:
         self.cr.Click_Create_Requisition_Sidebar()
        except:
            self.cr.Click_Requisition_Dropdown()
            self.cr.Click_Create_Requisition_Sidebar()

        # Select Warehouse
        self.cr.Select_Warehouse("ware1")

        # Select Department
        self.cr.Select_Department("sale")

        #Enter Document number
        self.cr.Enter_Document_number("Test123")

        #Enter version Number
        self.cr.Enter_Version_number("123")

        #Enter purpose
        self.cr.Enter_Purpose("Test")

        #Add product Rice
        self.cr.Add_Product("Rice")
        #EditProdt Rice
        self.cr.Editproduct1("100","KiloGram","TestRice")

        # Add product Black Pepper Whole
        self.cr.Add_Product("Black Pepper Whole")
        # EditProdt Black Pepper Whole
        self.cr.Editproduct2("1000","KiloGram","TestBlackPepperWhole")

        #Requisition Submit
        self.cr.Requisition_Submit()
        ExpectedURL ="http://qa.coolmindsinc.com/plantrich-qa/#/home/requisitions/viewAll-requisition"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False

class Test_002_CreateRequisition:

    @pytest.mark.regression
    @pytest.mark.run(order=7)
    def test_CreateReq_Negative_nullDataInput(self,setup):
        #Login
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        #Click Create Req
        self.cr = CreateRequisition(self.driver)#classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        try:
         self.cr.Click_Create_Requisition_Sidebar()
        except:
            self.cr.Click_Requisition_Dropdown()
            self.cr.Click_Create_Requisition_Sidebar()

        #Requisition Submit
        self.cr.Requisition_Submit()
        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/requisitions/viewAll-requisition"
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            self.driver.close()

    @pytest.mark.regression
    @pytest.mark.run(order=8)
    def test_Check_Back_Button(self,setup):
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.lp.login()

        # Click Create Req
        self.cr = CreateRequisition(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        self.cr.Click_Create_Requisition_Sidebar()

        # Press BackButton
        self.cr.Check_Back_Button()
        ExpectedURL ="http://qa.coolmindsinc.com/plantrich-qa/#/home/requisitions/viewAll-requisition"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            #To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False