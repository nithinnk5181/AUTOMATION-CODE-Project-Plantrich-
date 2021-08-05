from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep

class CreateRequisition:
    '''PageObjectives'''
    MENU_ICON="//button[2]"
    MENU_ICON1="//button[2]/span"

    REQUISITION_DROPDOWN_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[4]/a"
    CREATE_REQUISITION_SIDEBAR_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[4]/app-sidebar-nav-items/app-sidebar-nav-link[1]/a/app-sidebar-nav-link-content"
    WAREHOUSE_TEXTINPUT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/mat-form-field/div[1]/mat-form-field/input"
    WAREHOUSE_DATA_SELECT="//mat-option[@class='mat-option mat-focus-indicator ng-star-inserted']/span[@class='mat-option-text']"
    DEPARTMENT_SELECTION_XPATH="//*[@id='select1']"
    DOCUMENT_NUMBER_TEXTBOX_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[1]/div[2]/input"
    VERSION_NUMBER_TEXTBOX_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/mat-form-field/div[2]/input"
    PURPOSE_TEXTAREA_TEXTBOX_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[3]/div[2]/textarea"
    ADD_PRODUCT_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[4]/button[1]"
    SEARCH_PRODUCT_LABEL_XPATH="/html/body/div[2]/div[2]/div/mat-dialog-container/app-search-products/div/div[2]/div/div[2]/form/mat-form-field/div/mat-form-field/input"
    PRODUCT_DATA_SELECT="//mat-option"
    PRODUCT_DATA_SELECT_secondary="//mat-option/span"
    PRODUCT1_QUANTITY_TEXTBOX="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[5]/table/tbody/tr[1]/td[2]/input"
    PRODUCT1_DESCRIPTION_TEXTBOX="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[5]/table/tbody/tr[1]/td[4]/input"
    PRODUCT1_QUANTITY_TYPE_XPATH="//select[@id='select1' and @class='form-control ng-untouched ng-pristine ng-valid']"
    PRODUCT2_QUANTITY_TEXTBOX ="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[5]/table/tbody/tr[2]/td[2]/input"
    PRODUCT2_DESCRIPTION_TEXTBOX ="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[2]/form/div[5]/table/tbody/tr[2]/td[4]/input"
    PRODUCT2_QUANTITY_TYPE_XPATH ="//select[@id='select1' and @class='form-control ng-untouched ng-pristine ng-valid']"
    CREATE_REQUISITION_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[1]/div/button[1]"
    BACK_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-requisition-create/div/div[2]/div/div[1]/div/button[2]"

    def __init__(self,driver):
        self.driver=driver

    def Click_MenuIcon(self):
        try:
            self.driver.find_element_by_xpath(self.MENU_ICON).click()
        except:
            self.driver.find_element_by_xpath(self.MENU_ICON1).click()


    def Click_Requisition_Dropdown(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.REQUISITION_DROPDOWN_XPATH).click()

    def Click_Create_Requisition_Sidebar(self):
        sleep(1)
        self.driver.find_element_by_xpath(self.CREATE_REQUISITION_SIDEBAR_XPATH).click()

    def Select_Warehouse(self, warehouse):
        self.driver.find_element_by_xpath(self.WAREHOUSE_TEXTINPUT_XPATH).click()
        self.driver.find_element_by_xpath(self.WAREHOUSE_TEXTINPUT_XPATH).send_keys(warehouse)
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.WAREHOUSE_DATA_SELECT)))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def Select_Department(self,indexvalue):
        select1 = Select(self.driver.find_element_by_xpath(self.DEPARTMENT_SELECTION_XPATH))
        select1.select_by_visible_text(indexvalue)

    def Enter_Document_number(self, DocumentNumber):
        self.driver.find_element_by_xpath(self.VERSION_NUMBER_TEXTBOX_XPATH).send_keys(DocumentNumber)

    def Enter_Version_number(self, Versionnumber):
        self.driver.find_element_by_xpath(self.DOCUMENT_NUMBER_TEXTBOX_XPATH).send_keys(Versionnumber)

    def Enter_Purpose(self, purpose):
        self.driver.find_element_by_xpath(self.PURPOSE_TEXTAREA_TEXTBOX_XPATH).send_keys(purpose)

    def Add_Product(self,product):
        self.driver.find_element_by_xpath(self.ADD_PRODUCT_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.SEARCH_PRODUCT_LABEL_XPATH).click()
        self.driver.find_element_by_xpath(self.SEARCH_PRODUCT_LABEL_XPATH).send_keys(product)
        try:
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.PRODUCT_DATA_SELECT)))
            try:
                element.click()
            except:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                actions.click().perform()
        except:
            element1 = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.PRODUCT_DATA_SELECT_secondary)))
            element1.click()

    def Editproduct1(self,Quantity,QuantityType,Description):
        #Quantity
        self.driver.find_element_by_xpath(self.PRODUCT1_QUANTITY_TEXTBOX).send_keys(Quantity)
        # Quantity type
        select2 = Select(self.driver.find_element_by_xpath(self.PRODUCT1_QUANTITY_TYPE_XPATH))
        select2.select_by_visible_text(QuantityType)
        #Description
        self.driver.find_element_by_xpath(self.PRODUCT1_DESCRIPTION_TEXTBOX).send_keys(Description)

    def Editproduct2(self,Quantity,QuantityType,Description):
        #Quantity
        self.driver.find_element_by_xpath(self.PRODUCT2_QUANTITY_TEXTBOX).send_keys(Quantity)
        # Quantity type
        select2 = Select(self.driver.find_element_by_xpath(self.PRODUCT2_QUANTITY_TYPE_XPATH))
        select2.select_by_visible_text(QuantityType)
        #Description
        self.driver.find_element_by_xpath(self.PRODUCT2_DESCRIPTION_TEXTBOX).send_keys(Description)

    def Requisition_Submit(self):
        self.driver.find_element_by_xpath(self.CREATE_REQUISITION_BUTTON_XPATH).click()

    def Check_Back_Button(self):
        self.driver.find_element_by_xpath(self.BACK_BUTTON_XPATH).click()