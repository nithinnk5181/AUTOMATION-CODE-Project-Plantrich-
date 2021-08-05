from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


class Material_Storage:
    """PageObjectives"""
    MATERIAL_STORAGE_MENUITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[7]/a"
    CREATE_MATERIAL_STORAGE_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[7]/app-sidebar-nav-items/app-sidebar-nav-link[1]/a"
    INWARD_NO_OR_PO_NO_TXT_XPATH = "/html/body/app-root/app-dashboard/div/main/div/app-material-inward-to-storage/div/div/div/div[2]/form/div[1]/mat-form-field/div[2]/input"
    LATTEST_MATERIAL_STORAGE_XPATH = "//div/div/mat-option[last()]/span"
    PROD1_STORAGE_ACTION = "//tr[1]/td/div[@class='ng-star-inserted']/div/div[1]/*[name()='svg']"
    PROD2_STORAGE_ACTION = "//tr[2]/td/div[@class='ng-star-inserted']/div/div[1]/*[name()='svg']"

    ANALYSIS_NO_TXT_XPATH="//div[@class='form-group row'][3]/div[2]/input"
    NATURE_OF_ANALYSIS_TXT_XPATH="//div[@class='form-group row'][3]/div[4]/input"
    ANALYSIS_DOCUMENT_DATE_XPATH="//div[@class='form-group row'][3]/div[6]/div/input"

    DATE_SELECT_XPATH="//table[@class='days weeks']/tbody/tr[1]/td/span[text()='1']"

    ORGANIC_LABEL_PASTED_TXT_XPATH="//div[@class='form-group row'][6]/div[2]/input"
    BATCH_TXT_XPATH="//div[@class='form-group row'][6]/div[4]/input"
    DATE1_XPATH="//div[@class='form-group row'][6]/div[6]/div/input"

    LOCATION_TXT_XPATH="//div[@class='form-group row'][9]/div[2]/input"
    RACK_NO_TXT_XPATH="//div[@class='form-group row'][9]/div[4]/input"
    DATE2_XPATH="//div[@class='form-group row'][9]/div[6]/div/input"

    MATERIAL_NAME_TXT_XPATH="//div[@class='form-group row'][12]/div[2]/input"
    BATCH_NO_TXT_XPATH="//div[@class='form-group row'][12]/div[4]/input"
    QUANTITY_TXT_XPATH="//div[@class='form-group row'][12]/div[6]/input"

    MATERIAL_SHIFTED_BY_TXT_XPATH="//div[@class='form-group row'][14]/div[2]/input"
    VERIFIED_BY_TXT_XPATH="//div[@class='form-group row'][14]/div[4]/input"
    EMPLOYEE_CODE_TXT_XPATH="//div[@class='form-group row'][14]/div[6]/input"

    CREATE_BUTTON_XPATH="//div[@class='col-sm-8 ng-star-inserted']/button"

    FINAL_SUBMIT_BUTTON_XPATH="//div/div/div/div/button[@type='submit']"


    def __init__(self,driver):
        self.driver=driver

    def Click_on_Material_Storage(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.MATERIAL_STORAGE_MENUITEM_XPATH).click()

    def Click_Create_material_storage(self):
        sleep(3)
        self.driver.find_element_by_xpath(self.CREATE_MATERIAL_STORAGE_XPATH).click()

    def Select_lattest_material_inw_num(self,num):
        self.driver.find_element_by_xpath(self.INWARD_NO_OR_PO_NO_TXT_XPATH).send_keys(num)
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LATTEST_MATERIAL_STORAGE_XPATH)))
            element.click()
        except StaleElementReferenceException:
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.LATTEST_MATERIAL_STORAGE_XPATH)))
            element.click()

    def Select_Product1(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PROD1_STORAGE_ACTION)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()


    def Select_Product2(self):
        sleep(3)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PROD2_STORAGE_ACTION)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Add_data(self,Test,Test1):
        sleep(3)
        self.driver.find_element_by_xpath(self.ANALYSIS_NO_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.NATURE_OF_ANALYSIS_TXT_XPATH).send_keys(Test)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ANALYSIS_DOCUMENT_DATE_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        self.driver.find_element_by_xpath(self.DATE_SELECT_XPATH).click()

        self.driver.find_element_by_xpath(self.ORGANIC_LABEL_PASTED_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.BATCH_TXT_XPATH).send_keys(Test)


        self.driver.find_element_by_xpath(self.LOCATION_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.RACK_NO_TXT_XPATH).send_keys(Test)


        self.driver.find_element_by_xpath(self.MATERIAL_NAME_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.BATCH_NO_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.QUANTITY_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.QUANTITY_TXT_XPATH).send_keys(Test1)

        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DATE1_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        self.driver.find_element_by_xpath(self.DATE_SELECT_XPATH).click()

        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DATE2_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        self.driver.find_element_by_xpath(self.DATE_SELECT_XPATH).click()

        self.driver.find_element_by_xpath(self.MATERIAL_SHIFTED_BY_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.VERIFIED_BY_TXT_XPATH).send_keys(Test)
        self.driver.find_element_by_xpath(self.EMPLOYEE_CODE_TXT_XPATH).send_keys(Test)

    def Submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON_XPATH).click()

    def FinalSubmit(self):
        sleep(3)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.FINAL_SUBMIT_BUTTON_XPATH)))
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()
        except:
            self.driver.execute_script("arguments[0].click();", element)




