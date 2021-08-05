from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Create_PO:
    '''Page objectives'''
    PURCHASE_ORDER_MENUITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[5]/a"
    CREATE_PO_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[5]/app-sidebar-nav-items/app-sidebar-nav-link[1]/a/app-sidebar-nav-link-content"
    SEARCH_REQUISITION_LABEL_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-purchase-order/div/div[2]/div/div[2]/form/div[1]/div[2]/input"
    SEARCH_REQUISITION_SEARCHBAR_XPATH='/html/body/div[2]/div[2]/div/mat-dialog-container/app-search-requisition/div/div[2]/div/div[2]/form/mat-form-field/div/mat-form-field/input'
    LAST_REQUISITION_XPATH="//div[@class='cdk-overlay-pane']/div/mat-option[last()]/span"
    MOT_SELECT_XPATH='//*[@id="select1"]'
    DELIVARY_LOCATION_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-purchase-order/div/div[2]/div/div[2]/form/div[2]/div[3]/div[1]/mat-form-field/input"
    SELECT_FIRST_DELIVARY_LOCATION_XPATH="//div[@class='cdk-overlay-container']/div/div/div/mat-option[1]/span"
    PAYMENT_TERMS_TXT_XPATH='//*[@id="textarea-input"]'
    ETA_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-purchase-order/div/div[2]/div/div[2]/form/div[2]/div[6]/div[1]/div/button"
    NEXT_MONTH_BUTTON_XPATH="/html/body/bs-datepicker-container/div/div/div/div/bs-days-calendar-view/bs-calendar-layout/div[1]/bs-datepicker-navigation-view/button[4]/span"
    DATE_SELECT_XPATH="//table[@class='days weeks']/tbody/tr[1]/td/span[text()='1']"
    IGST_SELECT_XPATH="//div/select[@class='form-control ng-untouched ng-pristine ng-valid']"
    FREIGHT_SELECT_XPATH="//div/select[@class='form-control ng-untouched ng-pristine ng-invalid' and @formcontrolname='freight']"
    SUBMIT_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-create-purchase-order/div/div[2]/div/div[1]/div/div/button"

    def __init__(self,driver):
        self.driver=driver

    def Click_PURCHASE_ORDER(self):
        sleep(3)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PURCHASE_ORDER_MENUITEM_XPATH)))
        element.click()

    def Click_Create_PO(self):
        self.driver.find_element_by_xpath(self.CREATE_PO_ITEM_XPATH).click()

    def Click_Search_requisition(self,Reqnum):
        self.driver.find_element_by_xpath(self.SEARCH_REQUISITION_LABEL_XPATH).click()
        self.driver.find_element_by_xpath(self.SEARCH_REQUISITION_SEARCHBAR_XPATH).send_keys(Reqnum)

    def Click_Select_requisition(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LAST_REQUISITION_XPATH)))
        element.click()

    def Select_MOT(self,MOT):
        select=Select(self.driver.find_element_by_xpath(self.MOT_SELECT_XPATH))
        select.select_by_visible_text(MOT)

    def Enter_delivary_location(self,DEL):
        self.driver.find_element_by_xpath(self.DELIVARY_LOCATION_TXT_XPATH).click()
        self.driver.find_element_by_xpath(self.DELIVARY_LOCATION_TXT_XPATH).send_keys(DEL)
        self.driver.find_element_by_xpath(self.SELECT_FIRST_DELIVARY_LOCATION_XPATH).click()

    def Payment_terms(self,PT):
        self.driver.find_element_by_xpath(self.PAYMENT_TERMS_TXT_XPATH).send_keys(PT)

    def Select_ETA(self):
        self.driver.find_element_by_xpath(self.ETA_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.NEXT_MONTH_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.DATE_SELECT_XPATH).click()

    def Select_IGST(self,IGST):
        select = Select(self.driver.find_element_by_xpath(self.IGST_SELECT_XPATH))
        select.select_by_visible_text(IGST)

    def Select_Freight(self,freight):
        select = Select(self.driver.find_element_by_xpath(self.FREIGHT_SELECT_XPATH))
        select.select_by_visible_text(freight)

    def Create_PO_submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_XPATH).click()

    def get_popup_msg(self):
        text=self.driver.find_element_by_tag_name("body").text
        return text







