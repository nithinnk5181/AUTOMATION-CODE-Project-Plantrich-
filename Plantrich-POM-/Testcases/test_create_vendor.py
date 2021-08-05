#  pytest -v -s --html=Reports/test_create_vendor_report.html --self-contained-html Testcases/test_create_vendor.py --browser Firefox
#  pytest -v -s Testcases/test_create_vendor.py --browser Firefox
#  pytest -v -s Testcases/test_create_vendor.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Create_vendor import CreateVendor
from Utilities.readproperties import ReadConfig
from Prerequirments.Prerequirments import PREREQUIRMENTS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pytest
from time import sleep


BASEURL=ReadConfig.getBaseuRL()

class Test_001_Create_Vendor:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=31)
    def test_Ceate_Vendor_success(self,setup):
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.cv = CreateVendor(self.driver)  # classObject
        self.lp.login()

        #Click createVendor
        self.cr = CreateRequisition(self.driver)  # classObject
        try:
            self.cv.Click_ManageVendor()
        except:
            self.cr.Click_MenuIcon()
            self.cv.Click_ManageVendor()
        self.cv.Click_Create_vendor()

        #First page
        self.USERNAME="Test_"+self.cv.random_generator() #cReating Random Username
        self.cv.Enter_Username(self.USERNAME)
        self.cv.Enter_FullName("xyzabc")
        self.cv.Enter_Password("1234556")
        self.cv.Enter_password_confirmation("1234556")
        self.cv.Enter_Address1("testaddress")
        self.cv.Enter_Address2("testaddress1")
        self.cv.Enter_Pincode("679503")
        self.cv.Enter_Mobile("8086465181")
        self.cv.Enter_Phone("876689")

        self.EMAIL = self.cv.random_generator()+"@gmail.com" #cReating Random email id
        self.cv.Enter_Email(self.EMAIL)
        self.cv.Enter_Gst("18")
        self.cv.Enter_Description("Test")
        self.cv.Enter_anual_prod_capasity("1900")
        self.cv.Select_Geographic_area()
        self.cv.Select_Buisness_type()
        self.cv.Select_Buisness_nature()
        self.cv.Select_Product_nature()
        self.cv.Select_PVTPU()
        self.cv.Click_on_next()

        #Second page
        self.cv.Enter_Bank_name("Punjab National Bank")
        self.cv.Enter_Branch_name("Kakkanad")
        self.cv.Enter_Account_name("Savings")
        self.cv.Enter_IFSC_code("PUNB0591200")

        self.Account_number = random.randint(1111111111111111, 9999999999999999) # cReating Random AccountNumber
        self.cv.Enter_Account_num(self.Account_number)
        self.cv.Click_next2()

        # Third page
        self.cv.Enter_person_name("Test user")

        self.email = self.cv.random_generator() + "@gmail.com"  # cReating Random email id
        self.cv.Enter_person_email(self.email)
        self.cv.Enter_person_mobile("8086465182")
        self.cv.Enter_person_phone("676535")
        self.cv.Click_next_3()

        # Fourth page
        self.cv.Click_next_4()

        #Final submission
        self.cv.Click_Final_submission_button()

        ExpectedURL="http://qa.coolmindsinc.com/plantrich-qa/#/home/vendor-management/view-vendor"
        try:
            WebDriverWait(self.driver, 15).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
        except:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        self.cv.Goto_last_page()
        Username = self.cv.get_last_vendor_username()
        if Username == self.USERNAME:
            self.driver.close()
            assert True
        else:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False

class Test_002_Create_Vendor:

    @pytest.mark.regression
    @pytest.mark.run(order=32)
    def test_Create_Vendor_fail_with_null_input(self,setup):
        #Login
        self.driver=setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)#classObject
        self.cv = CreateVendor(self.driver)  # classObject
        self.lp.login()

        #Click createVendor
        self.cr = CreateRequisition(self.driver)  # classObject
        try:
            self.cv.Click_ManageVendor()
        except:
            self.cr.Click_MenuIcon()
            self.cv.Click_ManageVendor()
        self.cv.Click_Create_vendor()

        #First page
        self.USERNAME="Test_"+self.cv.random_generator() #cReating Random Username
        self.cv.Enter_Username("")
        self.cv.Enter_FullName("")
        self.cv.Enter_Password("")
        self.cv.Enter_password_confirmation("")
        self.cv.Enter_Address1("")
        self.cv.Enter_Address2("")
        self.cv.Enter_Pincode("")
        self.cv.Enter_Mobile("")
        self.cv.Enter_Phone("")

        self.EMAIL = self.cv.random_generator()+"@gmail.com" #cReating Random email id
        self.cv.Enter_Email("")
        self.cv.Enter_Gst("")
        self.cv.Enter_Description("")
        self.cv.Enter_anual_prod_capasity("")
        self.cv.Select_Geographic_area()
        self.cv.Select_Buisness_type()
        self.cv.Select_Buisness_nature()
        self.cv.Select_Product_nature()
        self.cv.Select_PVTPU()
        self.cv.Click_on_next()

        # Second page
        try:
            self.cv.Enter_Bank_name("Punjab National Bank")
            self.cv.Enter_Bank_name("Punjab National Bank")
            self.cv.Enter_Branch_name("Kakkanad")
            self.cv.Enter_Account_name("Savings")
            self.cv.Enter_IFSC_code("PUNB0591200")

            self.Account_number = random.randint(1111111111111111, 9999999999999999) # cReating Random AccountNumber
            self.cv.Enter_Account_num(self.Account_number)
            self.cv.Click_next2()

            # Third page
            self.cv.Enter_person_name("Test user")

            self.email = self.cv.random_generator() + "@gmail.com"  # cReating Random email id
            self.cv.Enter_person_email(self.email)
            self.cv.Enter_person_mobile("8086465182")
            self.cv.Enter_person_phone("676535")
            self.cv.Click_next_3()

            # Fourth page
            self.cv.Click_next_4()

            #Final submission
            self.cv.Click_Final_submission_button()

            ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/vendor-management/view-vendor"
            try:
                WebDriverWait(self.driver, 15).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            except:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
            self.cv.Goto_last_page()
            Username = self.cv.get_last_vendor_username()
            if Username == self.USERNAME:
                self.driver.close()
                assert True
            else:
                # To take the Screenshote
                PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
                assert False
        except:
            self.driver.close()
            assert True



