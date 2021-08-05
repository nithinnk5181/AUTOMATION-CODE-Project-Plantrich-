
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
import string
from time import sleep

class Add_product:

    """PageObjectives"""
    CATALOG_MENUiTEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[3]/a"
    PRODUCT_MENU_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[3]/app-sidebar-nav-items/app-sidebar-nav-link[4]/a"
    ADD_PRODUCT_BUTTON_XPATH="//div/button[text()='Add Product']"

    SKU_TXT_XPATH="//div/input[@id='defaultValue']"
    SET_NAME_SELECT_XPATH="//div/select[@id='selectedType']"
    STOCK_STATUS_SELECT_XPATH="//div/select[@id='selectedIsScope']"
    GST_SELECT_XPATH="//div/select[@id='taxValue']"
    CATAGORY_TXT_XPATH="//div//input[@placeholder='Enter a new tag']"

    ATTRIBUTES_BUTTON_XPATH="//ngb-accordion//div[@class='card-header']//button"
    NAME_TXT_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][1]//input"
    CODE_TXT_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][2]//input"
    DESCRIPTION_TXT_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][3]//input"
    PRICE_TXT_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][4]//input"
    WEIGHT_TXT_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][5]//input"
    VISIBILITY_YES_CHECK_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][6]//input[1]"
    HSN_CODE_TXT_XPATH="//ngb-accordion//div[@class='ng-star-inserted'][7]//input"
    SUBMIT_BUTTON_XPATH="//div//button[text()='Submit']"

    PAGE_COUNT_XPATH="//pagination-template//li"
    LAST_PAGE_XPATH="//pagination-template//li[last()]"
    LAST_ADDED_PRODUCT_NAME="//table//tr[last()]/td[1]"


    def __init__(self,driver):
        self.driver=driver

    def Click_on_Product(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.CATALOG_MENUiTEM_XPATH).click()
        self.driver.find_element_by_xpath(self.PRODUCT_MENU_ITEM_XPATH).click()

    def Click_Add_product(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ADD_PRODUCT_BUTTON_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Add_Data(self):

        self.driver.find_element_by_xpath(self.SKU_TXT_XPATH).send_keys(self.SKU)
        sleep(2)
        select=Select(self.driver.find_element_by_xpath(self.SET_NAME_SELECT_XPATH))
        select.select_by_visible_text("Default_1")
        sleep(2)
        select1 = Select(self.driver.find_element_by_xpath(self.STOCK_STATUS_SELECT_XPATH))
        select1.select_by_value("1")
        sleep(2)
        select2 = Select(self.driver.find_element_by_xpath(self.GST_SELECT_XPATH))
        select2.select_by_visible_text("9 + 9")


    def Add_Attributes(self,data1,data2):
        self.driver.find_element_by_xpath(self.ATTRIBUTES_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.NAME_TXT_XPATH).send_keys(self.SKU)
        self.driver.find_element_by_xpath(self.CODE_TXT_XPATH).send_keys(self.SKU)
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).send_keys(data1)
        self.driver.find_element_by_xpath(self.PRICE_TXT_XPATH).send_keys(data2)
        self.driver.find_element_by_xpath(self.WEIGHT_TXT_XPATH).send_keys(data2)
        self.driver.find_element_by_xpath(self.VISIBILITY_YES_CHECK_XPATH).click()
        self.driver.find_element_by_xpath(self.HSN_CODE_TXT_XPATH).send_keys(self.SKU)

    def Click_Submit(self):
        sleep(1)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    # Create Random string
    def Random_generator(size=5, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(5))

    SKU= "Test_" +Random_generator()

    def Goto_last_page(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = self.driver.find_elements_by_xpath(self.PAGE_COUNT_XPATH)
        num=len(Page_count)-4
        for i in range(num):
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LAST_PAGE_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()

    def Get_lattest_added_name(self):
        name=self.driver.find_element_by_xpath(self.LAST_ADDED_PRODUCT_NAME).text
        return name




