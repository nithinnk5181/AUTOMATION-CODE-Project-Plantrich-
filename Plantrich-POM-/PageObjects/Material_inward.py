from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Material_inward:
    """PageObjectives"""
    MATERIAL_INWARD_MENUiTEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-link[1]/a/app-sidebar-nav-link-content"
    LAST_CREATED_MATERIAL_INWARD_ID="//table/tbody/tr[1]/td[1]"
    CREATE_MATERIAL_INWARD_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-list-material-inward/div/div[1]/div/div[1]/div/button"
    PO_SEARCH_BOX_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/div[1]/div[2]/input"
    SUMBIT_PO_NUM_TXT_XPATH='//*[@id="mat-dialog-0"]/app-search-purchase-order/div/div[2]/div/div[2]/form/mat-form-field/div/mat-form-field/input'
    SELECT_LATTTEST_PO_XPATH="//div[@class='cdk-overlay-pane']/div[@class='mat-autocomplete-panel mat-autocomplete ng-star-inserted mat-autocomplete-visible']/mat-option[last()]/span"
    PROD1_DESCRIPTION_TXT_XPATH="//table/tbody/tr[1]/td[7]/textarea"
    PROD1_BATCH_NO_TXT_XPATH ="//table/tbody/tr[1]/td[8]/input"
    PROD1_BAG_COUNT_TXT_XPATH = "//table/tbody/tr[1]/td[9]/input"
    PROD2_DESCRIPTION_TXT_XPATH = "//table/tbody/tr[2]/td[7]/textarea"
    PROD2_BATCH_NO_TXT_XPATH = "//table/tbody/tr[2]/td[8]/input"
    PROD2_BAG_COUNT_TXT_XPATH = "//table/tbody/tr[2]/td[9]/input"

    BASIC_DETAILS_LINK_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div/button"
    VEHICLE_INWARD_REG_NO_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[1]/div[1]/input"
    VEH_NUM_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[2]/div[1]/input"
    DRIVER_PHONE_NUM_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[3]/div[1]/input"
    QLP_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[4]/div[1]/input"
    MATERIAL_INVOICE_NUM_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[1]/div[2]/input"
    DRIVER_NAME_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[2]/div[2]/input"
    SELECT_WAREHOUSE_XPATH="//div[@class='cdk-overlay-pane']/div/mat-option[1]/span"
    MATERIAL_UNLOADING_LOCATION_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[3]/div[2]/mat-form-field/input"
    QC_SAMPLED_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[1]/div/div[2]/div/form/div[4]/div[2]/input"

    CHECKLIST_DETAILS_LINK_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[2]/ngb-accordion[2]/div/div/button"
    UNIFORM_CHECK_XPATH="//div[@class='collapse show ng-star-inserted']/div[@class='card-body']/div/div[1]/div/div/input[@value='26']"
    CLEANED_HANDS_CHECK_XPATH="//div[@class='collapse show ng-star-inserted']/div[@class='card-body']/div/div[2]/div/div/input[@value='27']"
    SAFETY_MEASURES_CHECK_XPATH="//div[@class='collapse show ng-star-inserted']/div[@class='card-body']/div/div[3]/div/div/input[@value='28']"
    FREE_FROM_INSECTS_CHECK_XPATH="//div[@class='collapse show ng-star-inserted']/div[@class='card-body']/div/div[1]/div/div/input[@value='23']"
    FREE_FROM_DAMAGES_CHECK_XPATH="//div[@class='collapse show ng-star-inserted']/div[@class='card-body']/div/div[2]/div/div/input[@value='24']"
    PROPER_COVERING_CHECK_XPATH="//div[@class='collapse show ng-star-inserted']/div[@class='card-body']/div/div[3]/div/div/input[@value='25']"

    SAVE_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[1]/button"
    CREATE_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-material-inward/div/div/div/div[1]/div/button"

    POPUP_MSG="//*[text()='Material Inward Updated']"

    def __init__(self,driver):
        self.driver=driver

    def Click_material_inward(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.MATERIAL_INWARD_MENUiTEM_XPATH).click()

    def Click_Create_material_inward_button(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CREATE_MATERIAL_INWARD_BUTTON_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Serach_by_PO_num(self,PO):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PO_SEARCH_BOX_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element_by_xpath(self.SUMBIT_PO_NUM_TXT_XPATH).send_keys(PO)

    def Select_lattest_PO(self):
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.SELECT_LATTTEST_PO_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Add_product1_details(self,Desc,Batch_no,Bag_count):
        self.driver.find_element_by_xpath(self.PROD1_DESCRIPTION_TXT_XPATH).send_keys(Desc)
        self.driver.find_element_by_xpath(self.PROD1_BATCH_NO_TXT_XPATH).send_keys(Batch_no)
        self.driver.find_element_by_xpath(self.PROD1_BAG_COUNT_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PROD1_BAG_COUNT_TXT_XPATH).send_keys(Bag_count)

    def Add_product2_details(self,Desc,Batch_no,Bag_count):
        self.driver.find_element_by_xpath(self.PROD2_DESCRIPTION_TXT_XPATH).send_keys(Desc)
        self.driver.find_element_by_xpath(self.PROD2_BATCH_NO_TXT_XPATH).send_keys(Batch_no)
        self.driver.find_element_by_xpath(self.PROD2_BAG_COUNT_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PROD2_BAG_COUNT_TXT_XPATH).send_keys(Bag_count)

    def Add_basic_details(self,phonenum,testdata,ware):
        self.driver.find_element_by_xpath(self.BASIC_DETAILS_LINK_XPATH).click()
        self.driver.find_element_by_xpath(self.VEHICLE_INWARD_REG_NO_TXT_XPATH).send_keys(testdata)
        self.driver.find_element_by_xpath(self.VEH_NUM_TXT_XPATH).send_keys(testdata)
        self.driver.find_element_by_xpath(self.DRIVER_PHONE_NUM_TXT_XPATH).send_keys(phonenum)
        self.driver.find_element_by_xpath(self.QLP_TXT_XPATH).send_keys(testdata)
        self.driver.find_element_by_xpath(self.MATERIAL_INVOICE_NUM_TXT_XPATH).send_keys(testdata)
        self.driver.find_element_by_xpath(self.DRIVER_NAME_TXT_XPATH).send_keys(testdata)
        self.driver.find_element_by_xpath(self.QC_SAMPLED_TXT_XPATH).send_keys(testdata)
        self.driver.find_element_by_xpath(self.MATERIAL_UNLOADING_LOCATION_XPATH).send_keys(ware)
        self.driver.find_element_by_xpath(self.SELECT_WAREHOUSE_XPATH).click()

    def Add_Checklist_details(self):
        self.driver.find_element_by_xpath(self.CHECKLIST_DETAILS_LINK_XPATH).click()
        self.driver.find_element_by_xpath(self.UNIFORM_CHECK_XPATH).click()
        self.driver.find_element_by_xpath(self.CLEANED_HANDS_CHECK_XPATH).click()
        self.driver.find_element_by_xpath(self.SAFETY_MEASURES_CHECK_XPATH).click()

        self.driver.find_element_by_xpath(self.FREE_FROM_INSECTS_CHECK_XPATH).click()
        self.driver.find_element_by_xpath(self.FREE_FROM_DAMAGES_CHECK_XPATH).click()
        self.driver.find_element_by_xpath(self.PROPER_COVERING_CHECK_XPATH).click()

    def Click_save(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON_XPATH).click()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def get_LAST_CREATED_MATERIAL_INWARD_ID(self):
        id=self.driver.find_element_by_xpath(self.LAST_CREATED_MATERIAL_INWARD_ID).text
        return id


