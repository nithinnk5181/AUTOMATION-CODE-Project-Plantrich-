from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.action_chains import ActionChains
import string
from time import sleep

class CreateVendor:
    '''PageObjectives'''
    VENDOR_MANAGEMENT_MENU_ICON_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[12]/a"
    CREATE_VENDOR_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[12]/app-sidebar-nav-items/app-sidebar-nav-link[1]/a"
    USERNAME_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='username' ]"
    FULL_NAME_TXT_XPATH ="//div[@class='col-md-4']/input[@placeholder='Name' ]"
    PASSWORD_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='password' ]"
    CONFIRM_PASSWORD_TXT_XPATH ="//div[@class='col-md-4']/input[@placeholder='confirmPassword' ]"
    ADDRESS_LINE1_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='Address'  and  @formcontrolname='address1']"
    ADDRESS_LINE2_TXT_XPATH = "//div[@class='col-md-4']/input[@placeholder='Address'  and  @formcontrolname='address2']"
    PINCODE_TXT_XPATH ="//div[@class='col-md-4']/input[@placeholder='Pincode']"
    MOBILE_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='Mobile']"
    PHONE_TXT_XPATH ="//div[@class='col-md-4']/input[@placeholder='Phone']"
    EMAIL_TXT_XPATH ="//div[@class='col-md-4']/input[@placeholder='Email id']"
    GST_TXT_XPATH ="//div[@class='col-md-4']/input[@placeholder='GST']"
    DESCRIPTION_TXT_XPATH ="//div[@class='col-sm-4']/input[@placeholder='Description']"
    ANNUAL_PRODUCTION_CAPASITY_TXT_XPATH ="//div[@class='col-md-4']/input[@class='form-control ng-untouched ng-pristine ng-invalid' and  @placeholder='Annual Production Capacity']"
    GEOGRAPHIC_AREA_DROPDOWN_XPATH='//*[@id="geographicDetails"]'
    BUISNESS_TYPE_DROPDOWN_XPATH = '//*[@id="businessType"]'
    BUISNESS_NATURE_DROPDOWN_XPATH = '//*[@id="businessNature"]'
    PRODUCT_NATURE_DROPDOWN_XPATH = '//*[@id="ProdctNature"]'
    PVTPU_XPATH = '//*[@id="physicalVisit"]'
    NEXT_BUTTON_CSS_SELECTOR="button.btn:nth-child(2)"

    BANK_NAME_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='Bank Name']"
    BRANCH_NAME_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='Branch Name']"
    ACCOUNT_NAME_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='Account Name']"
    IFSC_CODE_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='IFSC Code']"
    ACCOUNT_NUMBER_TXT_XPATH="//div[@class='col-md-4']/input[@placeholder='IFSC Code']"
    NEXT2_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-vendor-management/div/div/div/div[2]/mat-horizontal-stepper/div[2]/div[2]/form/div[6]/div/button[2]"

    PERSON_NAME_TXT_XPATH="//div[@class='col-sm-4']/input[@class='form-control ng-untouched ng-pristine ng-invalid' and @placeholder='Person Name']"
    PERSON_EMAIL_TXT_XPATH="//div[@class='col-sm-4']/input[@class='form-control ng-untouched ng-pristine ng-invalid' and @placeholder='Person Email']"
    PERSON_MOBILE_TXT_XPATH="//div[@class='col-sm-4']/input[@class='form-control ng-untouched ng-pristine ng-invalid' and @placeholder='Person Mobile']"
    PERSON_PHONE_TXT_XPATH="//div[@class='col-sm-4']/input[@class='form-control ng-untouched ng-pristine ng-invalid' and @placeholder='Person Phone']"
    NEXT3_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-vendor-management/div/div/div/div[2]/mat-horizontal-stepper/div[2]/div[3]/div/div/button[2]"

    NEXT4_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-vendor-management/div/div/div/div[2]/mat-horizontal-stepper/div[2]/div[4]/div[2]/div/button[2]"

    FINAL_SUBMISSION_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-vendor-management/div/div/div/div[2]/mat-horizontal-stepper/div[2]/div[5]/div/div/button[2]"
    VENDOR_TABLE_LAST_RAW="//table/tbody/tr[last()]/td[3]"

    LAST_PAGE_XPATH = "//ngb-pagination//li[last()]/a"
    PAGE_COUNT_XPATH="//ngb-pagination//li"


    def __init__(self,driver):
        self.driver=driver

    def Click_ManageVendor(self):
        sleep(2)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.VENDOR_MANAGEMENT_MENU_ICON_XPATH)))
        element.click()

    def Click_Create_vendor(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.CREATE_VENDOR_ITEM_XPATH).click()

    #First page
    def Enter_Username(self,username):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.USERNAME_TXT_XPATH)))
        element.click()
        self.driver.find_element_by_xpath(self.USERNAME_TXT_XPATH).send_keys(username)

    def Enter_FullName(self,Fullname):
        self.driver.find_element_by_xpath(self.FULL_NAME_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.FULL_NAME_TXT_XPATH).send_keys(Fullname)

    def Enter_Password(self,password):
        self.driver.find_element_by_xpath(self.PASSWORD_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PASSWORD_TXT_XPATH).send_keys(password)

    def Enter_password_confirmation(self,password):
        self.driver.find_element_by_xpath(self.CONFIRM_PASSWORD_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.CONFIRM_PASSWORD_TXT_XPATH).send_keys(password)

    def Enter_Address1(self,Address1):
        self.driver.find_element_by_xpath(self.ADDRESS_LINE1_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.ADDRESS_LINE1_TXT_XPATH).send_keys(Address1)

    def Enter_Address2(self,Address1):
        self.driver.find_element_by_xpath(self.ADDRESS_LINE2_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.ADDRESS_LINE2_TXT_XPATH).send_keys(Address1)

    def Enter_Pincode(self,pincode):
        self.driver.find_element_by_xpath(self.PINCODE_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PINCODE_TXT_XPATH).send_keys(pincode)

    def Enter_Mobile(self, mobile):
        self.driver.find_element_by_xpath(self.MOBILE_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.MOBILE_TXT_XPATH).send_keys(mobile)

    def Enter_Phone(self, phone):
        self.driver.find_element_by_xpath(self.PHONE_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PHONE_TXT_XPATH).send_keys(phone)

    def Enter_Email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.EMAIL_TXT_XPATH).send_keys(email)

    def Enter_Gst(self, gst):
        self.driver.find_element_by_xpath(self.GST_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.GST_TXT_XPATH).send_keys(gst)

    def Enter_Description(self, desc):
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).send_keys(desc)

    def Enter_anual_prod_capasity(self, apc):
        self.driver.find_element_by_xpath(self.ANNUAL_PRODUCTION_CAPASITY_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.ANNUAL_PRODUCTION_CAPASITY_TXT_XPATH).send_keys(apc)

    def Select_Geographic_area(self):
        select = Select(self.driver.find_element_by_xpath(self.GEOGRAPHIC_AREA_DROPDOWN_XPATH))
        select.select_by_visible_text("Kochi")

    def Select_Buisness_type(self):
        select = Select(self.driver.find_element_by_xpath(self.BUISNESS_TYPE_DROPDOWN_XPATH))
        select.select_by_visible_text("NORMAL")

    def Select_Buisness_nature(self):
        select = Select(self.driver.find_element_by_xpath(self.BUISNESS_NATURE_DROPDOWN_XPATH))
        select.select_by_visible_text("WHOLESALE")

    def Select_Product_nature(self):
        select = Select(self.driver.find_element_by_xpath(self.PRODUCT_NATURE_DROPDOWN_XPATH))
        select.select_by_visible_text("Default")

    def Select_PVTPU(self):
        select = Select(self.driver.find_element_by_xpath(self.PVTPU_XPATH))
        select.select_by_visible_text("Yes")

    def Click_on_next(self):
        self.driver.find_element_by_css_selector(self.NEXT_BUTTON_CSS_SELECTOR).click()


    #Second page
    def Enter_Bank_name(self,bankname):
        self.driver.find_element_by_xpath(self.BANK_NAME_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.BANK_NAME_TXT_XPATH).send_keys(bankname)


    def Enter_Branch_name(self, branchname):
        self.driver.find_element_by_xpath(self.BRANCH_NAME_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.BRANCH_NAME_TXT_XPATH).send_keys(branchname)

    def Enter_Account_name(self, accountname):
        self.driver.find_element_by_xpath(self.ACCOUNT_NAME_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.ACCOUNT_NAME_TXT_XPATH).send_keys(accountname)

    def Enter_IFSC_code(self, IFSC):
        self.driver.find_element_by_xpath(self.IFSC_CODE_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.IFSC_CODE_TXT_XPATH).send_keys(IFSC)

    def Enter_Account_num(self, Ac_no):
        self.driver.find_element_by_xpath(self.ACCOUNT_NUMBER_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.ACCOUNT_NUMBER_TXT_XPATH).send_keys(Ac_no)

    def Click_next2(self,):
        self.driver.find_element_by_xpath(self.NEXT2_BUTTON_XPATH).click()

    #Third page
    def Enter_person_name(self, name):
        self.driver.find_element_by_xpath(self.PERSON_NAME_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PERSON_NAME_TXT_XPATH).send_keys(name)

    def Enter_person_email(self, email):
        self.driver.find_element_by_xpath(self.PERSON_EMAIL_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PERSON_EMAIL_TXT_XPATH).send_keys(email)

    def Enter_person_mobile(self, mobile):
        self.driver.find_element_by_xpath(self.PERSON_MOBILE_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PERSON_MOBILE_TXT_XPATH).send_keys(mobile)

    def Enter_person_phone(self, phone):
        self.driver.find_element_by_xpath(self.PERSON_PHONE_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PERSON_PHONE_TXT_XPATH).send_keys(phone)

    def Click_next_3(self):
        self.driver.find_element_by_xpath(self.NEXT3_BUTTON_XPATH).click()

    def Click_next_4(self):
        self.driver.find_element_by_xpath(self.NEXT4_BUTTON_XPATH).click()


    def Click_Final_submission_button(self):
        self.driver.find_element_by_xpath(self.FINAL_SUBMISSION_BUTTON_XPATH).click()

    def get_last_vendor_username(self):
        Username=self.driver.find_element_by_xpath(self.VENDOR_TABLE_LAST_RAW)
        return Username.text

    def Goto_last_page(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = self.driver.find_elements_by_xpath(self.PAGE_COUNT_XPATH)
        num=len(Page_count)
        for i in range(num):
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LAST_PAGE_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()

    # Create Random string
    def random_generator(size=5, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(5))


