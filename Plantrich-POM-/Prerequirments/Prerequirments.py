from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Approve_Requisition import ApproveRequisition
from PageObjects.Create_Quotes import CreateQuotes
from PageObjects.Approve_Quote import Approve_quote
from PageObjects.Create_PO import Create_PO
from PageObjects.Confirm_PO import Confirm_PO
from PageObjects.Material_inward import Material_inward
from PageObjects.Create_material_QC import Material_QC
from PageObjects.Material_storage import Material_Storage
from PageObjects.Approve_Storage import Approve_storage
from PageObjects.Create_vendor import CreateVendor
from selenium.common.exceptions import NoSuchElementException
from Utilities.readproperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import random
import pytest
import sys
BASEURL = ReadConfig.getBaseuRL()

class PREREQUIRMENTS:

    @staticmethod
    def TAKE_SCREENSHOTE(self):
        # To take the Screenshote
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        filename = "Plantrich "+ ".png"
        self.driver.save_screenshot("Screenshotes/" + filename)

    @staticmethod
    def LOGIN(setup):
        # Login
        driver = setup
        driver.get(BASEURL)
        lp = Login(driver)  # classObject
        lp.login()

    @staticmethod
    def CREATE_REQUISITION(self,setup):
        #Login
        self.browser=setup
        self.browser.get(BASEURL)
        self.lp = Login(self.browser)#classObject
        self.lp.login()

        #Click Create Req
        self.cr = CreateRequisition(self.browser)#classObject
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
            WebDriverWait(self.browser, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            print('Requistion created')
            assert True
        except:
            print("Requistion creation failed")
            assert False

    @staticmethod
    def APPROVE_REQUISITION(self,setup):

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
        self.ar.click_Approve_Button()
        # Check the URL
        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/requisitions/approve-requisition"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            try:
                RequisitionNumber_new = self.ar.get_table_data()
                if RequisitionNumber_new != RequisitionNumber:
                    print('Requistion Approved')
                    assert True
                else:
                    print("Requisition Approve failed")
                    assert False
            except NoSuchElementException:
                print("Requisition Approved")
            except:
                print("Requisition Approve failed")
                assert False
        except:
            print("Requisition Approve failed")
            assert False


    @staticmethod
    def CREATE_QUOTE(self,setup):
        # Login
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.login()

        # Click createQuote
        self.cr = CreateRequisition(self.driver)  # classObject
        self.cq = CreateQuotes(self.driver)  # classObject
        try:
            self.cr.Click_Requisition_Dropdown()
        except:
            self.cr.Click_MenuIcon()
            self.cr.Click_Requisition_Dropdown()
        self.cq.create_quote_click()
        RequisitionNumber = self.cq.get_latest_requisition_number()
        self.cq.click_action()
        self.cq.serch_vendor("Plantrich")
        self.cq.vendor_data_select()
        # add price
        self.cq.give_pricePROD1("20")
        self.cq.give_pricePROD2("30")
        # add note
        self.cq.give_note_PROD1("price added")
        self.cq.give_note_PROD2("PRICE ADDED")
        # submit
        self.cq.click_on_create_quote()

        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/requisition-quotes/requisitions-quotes"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            RequisitionNumber_new = self.cq.get_latest_requisition_number()
            if RequisitionNumber_new == RequisitionNumber:
                print("Quote created")
                assert True
            else:
                print("Quote creation failed")
                assert False
        except:
            print("Quote creation failed")
            assert False

    @staticmethod
    def APPROVE_QUOTE(self, setup):
        # Login
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.lp.login()

        # Click Approve_Quote
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

        # checking the quote is approved or not
        try:
            self.aq.Click_Approve_quote()
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            assert True
            self.driver.close()


    @staticmethod
    def CREATE_PO(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)  # classObject
        self.cr = CreateRequisition(self.driver)
        self.po = Create_PO(self.driver)

        # Login
        self.lp.login()

        # CreatePurchase Order
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
            print("PO created")
            assert True
        except:
            print("PO creation failed")
            assert False

    @staticmethod
    def CONFIRM_PO(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)  # classObject
        self.cr = CreateRequisition(self.driver)
        self.po = Create_PO(self.driver)
        self.cp = Confirm_PO(self.driver)

        # Login
        self.lp.login()

        # CreatePurchase Order
        try:
            self.po.Click_PURCHASE_ORDER()
        except:
            self.cr.Click_MenuIcon()
            self.po.Click_PURCHASE_ORDER()
        self.cp.Click_confirm_PO_item()
        lattest_POnum = self.cp.Get_lattest_PO_number()
        self.cp.Click_Action_lattest_PO()
        self.cp.Click_Approve_button()
        self.cp.Click_Approve_Confirm_yes()
        updated_PO_num = self.cp.Get_lattest_PO_number()
        if updated_PO_num == lattest_POnum:
            print("PO confirm failed")
            assert False
        else:
            print("PO Confirmed")
            assert True

    @staticmethod
    def CREATE_MATERIAL_INWARD(self,setup):

        self.driver = setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)  # classObject
        self.cr = CreateRequisition(self.driver)
        self.mi = Material_inward(self.driver)

        # Login
        self.lp.login()

        # CreatePurchase Order
        try:
            self.mi.Click_material_inward()
        except:
            self.cr.Click_MenuIcon()
            self.mi.Click_material_inward()
        lattest_created_id = self.mi.get_LAST_CREATED_MATERIAL_INWARD_ID()
        self.mi.Click_Create_material_inward_button()
        self.mi.Serach_by_PO_num("PURCHASE-")
        self.mi.Select_lattest_PO()
        self.mi.Add_product1_details("test", "123", "50")
        self.mi.Add_product2_details("Test", "321", "30")
        self.mi.Add_basic_details("8086564523", "Test", "ware1")
        self.mi.Add_Checklist_details()
        self.mi.Click_save()  # Save and submit

        lattest_updated_id = self.mi.get_LAST_CREATED_MATERIAL_INWARD_ID()
        if lattest_updated_id == lattest_created_id:
            print("Material inward creation failed")
            assert False
        else:
            print("Material inward created")
            assert True

    @staticmethod
    def CREATE_MATERIAL_QC(self, setup):

        self.driver = setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)  # classObject
        self.cr = CreateRequisition(self.driver)
        self.mq = Material_QC(self.driver)

        # Login
        self.lp.login()

        # CreatePurchase Order
        try:
            self.mq.Click_on_Material_qc()
        except:
            self.cr.Click_MenuIcon()
            self.mq.Click_on_Material_qc()
        self.mq.Click_on_Create_Material_qc()
        self.mq.Click_on_SearchBox('MIR-')
        self.mq.Select_lattest_MIR()
        self.mq.Prod1_action()
        self.mq.Add_data("test", "20")
        self.mq.Approve_QC()

        self.mq.Prod2_action()
        self.mq.Add_data("TEST", "30")
        self.mq.Approve_QC()

        self.mq.Prod2_action()
        Present = self.mq.Check_PrintButton()

        if Present == True:
            assert True
            print("QC created")
        else:
            print("QC creation failed")
            assert False

    @staticmethod
    def CREATE_MATERIAL_STORAGE(self, setup):

        self.driver = setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)  # classObject
        self.cr = CreateRequisition(self.driver)
        self.ms = Material_Storage(self.driver)

        # Login
        self.lp.login()

        # CreatePurchase Order
        try:
            self.ms.Click_on_Material_Storage()
        except:
            self.cr.Click_MenuIcon()
            self.ms.Click_on_Material_Storage()
        self.ms.Click_Create_material_storage()
        self.ms.Select_lattest_material_inw_num("MIR-")
        self.ms.Select_Product1()
        self.ms.Add_data("TEST", "100")
        self.ms.Submit()
        self.ms.Select_Product2()
        self.ms.Add_data("test", "100")
        self.ms.Submit()

        self.ms.FinalSubmit()

        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/material-storage/table-material-storage"
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
            print("Storage Created")
            assert True
        except:
            print("Storage Creation failed")
            assert False

    @staticmethod
    def APPROVE_MATERIAL_STORAGE(self, setup):
        self.driver = setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)  # classObject
        self.cr = CreateRequisition(self.driver)
        self.As = Approve_storage(self.driver)

        # Login
        self.lp.login()

        # CreatePurchase Order
        try:
            self.As.click_Approve_storage()
        except:
            self.cr.Click_MenuIcon()
            self.As.click_Approve_storage()
        lattestID = self.As.Get_lattest_id()
        self.As.Click_action()
        self.As.Approve()
        UpdatedID = self.As.Get_lattest_id()

        if UpdatedID == lattestID:
            print("Storage approve failed")

            assert False
        else:
            print("Storage approved")
            assert True

    @staticmethod
    def CREATE_VENDOR(self, setup):
        # Login
        self.driver = setup
        self.driver.get(BASEURL)
        self.lp = Login(self.driver)  # classObject
        self.cv = CreateVendor(self.driver)  # classObject
        self.lp.login()

        # Click createVendor
        self.cr = CreateRequisition(self.driver)  # classObject
        try:
            self.cv.Click_ManageVendor()
        except:
            self.cr.Click_MenuIcon()
            self.cv.Click_ManageVendor()
        self.cv.Click_Create_vendor()

        # First page
        self.USERNAME = "Test_" + self.cv.random_generator()  # cReating Random Username
        self.cv.Enter_Username(self.USERNAME)
        self.cv.Enter_FullName("xyzabc")
        self.cv.Enter_Password("1234556")
        self.cv.Enter_password_confirmation("1234556")
        self.cv.Enter_Address1("testaddress")
        self.cv.Enter_Address2("testaddress1")
        self.cv.Enter_Pincode("679503")
        self.cv.Enter_Mobile("8086465181")
        self.cv.Enter_Phone("876689")

        self.EMAIL = self.cv.random_generator() + "@gmail.com"  # cReating Random email id
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

        # Second page
        self.cv.Enter_Bank_name("Punjab National Bank")
        self.cv.Enter_Branch_name("Kakkanad")
        self.cv.Enter_Account_name("Savings")
        self.cv.Enter_IFSC_code("PUNB0591200")

        self.Account_number = random.randint(1111111111111111, 9999999999999999)  # cReating Random AccountNumber
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

        # Final submission
        self.cv.Click_Final_submission_button()

        ExpectedURL = "http://qa.coolmindsinc.com/plantrich-qa/#/home/vendor-management/view-vendor"
        try:
            WebDriverWait(self.driver, 15).until(EC.url_to_be(ExpectedURL))  # Wait for the next page to load
        except:
            print("Vendor_Creation_failed")
            assert False
        self.cv.Goto_last_page()
        Username = self.cv.get_last_vendor_username()
        if Username == self.USERNAME:
            print("Vendor Created")
            assert True
        else:
            print("Vendor_Creation_failed")
            assert False