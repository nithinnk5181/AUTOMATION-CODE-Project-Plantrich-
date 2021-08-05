from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Material_QC:

    """PageObjectives"""
    MATERIAL_QC_MENU_DROPDOWN_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[6]/a"
    CREATE_MATERIAL_QC_ITEM="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[6]/app-sidebar-nav-items/app-sidebar-nav-link/a/app-sidebar-nav-link-content"
    INWARD_NO_OR_PO_NO_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-vehicle-qc-checklist/div/div/div/div[2]/form/div[1]/mat-form-field/div[2]/input"
    LATTEST_MATERIAL_STORAGE_XPATH="//div/div/mat-option[last()]/span"
    PROD1_QC_ACTION="//tr[1]/td/div[@class='ng-star-inserted']/div/div/*[name()='svg']"
    PROD2_QC_ACTION="//tr[2]/td/div[@class='ng-star-inserted']/div/div/*[name()='svg']"

    NAME_OF_THE_TRANSPORTES="//form/div[3]/div[4]/input"
    VEHICLE_NUMBER="//form/div[4]/div[2]/input[@formcontrolname='vehicleNo']"
    CONTAINER_NUMBER="//form/div[4]/div[4]/input[@formcontrolname='containerNo']"
    MATERIAL_QA_CHECKLIST_1 ="//tr/div[@class='ng-star-inserted'][1]/div/td/input"
    MATERIAL_QA_CHECKLIST_2 = "//tr/div[@class='ng-star-inserted'][2]/div/td/input"
    MATERIAL_QA_CHECKLIST_3 = "//tr/div[@class='ng-star-inserted'][3]/div/td/input"
    MATERIAL_QA_CHECKLIST_4 = "//tr/div[@class='ng-star-inserted'][4]/div/td/input"
    MATERIAL_QA_CHECKLIST_5 = "//tr/div[@class='ng-star-inserted'][5]/div/td/input"
    MATERIAL_QA_CHECKLIST_6 = "//tr/div[@class='ng-star-inserted'][6]/div/td/input"
    MATERIAL_QA_CHECKLIST_7 = "//tr/div[@class='ng-star-inserted'][7]/div/td/input"
    MATERIAL_QA_CHECKLIST_8 = "//tr/div[@class='ng-star-inserted'][8]/div/td/input"
    MATERIAL_QA_CHECKLIST_9 = "//tr/div[@class='ng-star-inserted'][9]/div/td/input"

    CHECKED_BY_TXT_XPATH="//form/div[7]/div[2]/input[@formcontrolname='checkedBy']"
    VERIFIED_BY_TXT_XPATH="//form/div[7]/div[4]/input[@formcontrolname='verifiedBy']"
    ISSUED_BY_TXT_XPTAH="//form/div[8]/table/tr[2]/td[1]/input"
    APPROVED_BY_TXT_XPATH="//form/div[8]/table/tr[2]/td[2]/input"

    SUPPLIER_NAME_TXT_XPATH="//form/div[3]/div[2]/input"
    NO_OF_BAGS_TXT_XPATH="//form/div[4]/div[@class='col-md-6']/input"
    QUANTITY_TXT_XPATH="//form/div[5]/div[@class='col-md-6']/input"
    DELIVARY_NOTE_NUMBER="//form/div[6]/div[@class='col-md-6']/input"

    APPROVE_BUTTON_XPATH="//button[@class='btn btn-sm btn-success button-width col-sm-4']"
    DECLAIN_BUTTON_XPATH="//button[@class='btn btn-sm btn-danger button-width col-sm-4']"

    PRINT_BUTTON_XPATH="//button[@printsectionid='print-section']"


    def __init__(self,driver):
        self.driver=driver

    def Click_on_Material_qc(self):
        sleep(3)
        self.driver.find_element_by_xpath(self.MATERIAL_QC_MENU_DROPDOWN_XPATH).click()

    def Click_on_Create_Material_qc(self):
        self.driver.find_element_by_xpath(self.CREATE_MATERIAL_QC_ITEM).click()

    def Click_on_SearchBox(self,MIR):
        self.driver.find_element_by_xpath(self.INWARD_NO_OR_PO_NO_TXT_XPATH).send_keys(MIR)

    def Select_lattest_MIR(self):
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.LATTEST_MATERIAL_STORAGE_XPATH)))
        element.click()

    def Prod1_action(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PROD1_QC_ACTION)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Add_data(self,data,data2):
        self.driver.find_element_by_xpath(self.NAME_OF_THE_TRANSPORTES).send_keys(data)
        self.driver.find_element_by_xpath(self.VEHICLE_NUMBER).send_keys(data)
        self.driver.find_element_by_xpath(self.CONTAINER_NUMBER).send_keys(data)

        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_1).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_2).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_3).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_4).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_5).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_6).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_7).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_8).click()
        self.driver.find_element_by_xpath(self.MATERIAL_QA_CHECKLIST_9).click()

        self.driver.find_element_by_xpath(self.CHECKED_BY_TXT_XPATH).send_keys(data)
        self.driver.find_element_by_xpath(self.VERIFIED_BY_TXT_XPATH).send_keys(data)
        self.driver.find_element_by_xpath(self.ISSUED_BY_TXT_XPTAH).send_keys(data)
        self.driver.find_element_by_xpath(self.APPROVED_BY_TXT_XPATH).send_keys(data)

        self.driver.find_element_by_xpath(self.SUPPLIER_NAME_TXT_XPATH).send_keys(data)
        self.driver.find_element_by_xpath(self.NO_OF_BAGS_TXT_XPATH).send_keys(data2)
        self.driver.find_element_by_xpath(self.QUANTITY_TXT_XPATH).send_keys(data2)
        self.driver.find_element_by_xpath(self.DELIVARY_NOTE_NUMBER).send_keys(data2)

    def Prod2_action(self):
        sleep(3)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PROD2_QC_ACTION)))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def Approve_QC(self):
        self.driver.find_element_by_xpath(self.APPROVE_BUTTON_XPATH).click()

    def Declain_QC(self):
        self.driver.find_element_by_xpath(self.DECLAIN_BUTTON_XPATH).click()

    def Check_PrintButton(self):
        sleep(2)
        present=self.driver.find_element_by_xpath(self.PRINT_BUTTON_XPATH).is_displayed()
        return present
