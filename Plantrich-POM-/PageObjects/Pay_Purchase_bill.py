from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class Pay_Purchase_bill:

    """PageObjectives"""
    PAY_PURCHASE_BILL_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[5]/app-sidebar-nav-items/app-sidebar-nav-link[5]/a/app-sidebar-nav-link-content"
    SEARCH_PO_LABEL_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-view-purchase-order-payments/div/div[2]/div/div[2]/form/div[1]/div/div[2]/input"
    SEARCH_PO_TXT_XPATH="//div[@class='col-md-4']/mat-form-field/input"
    LATTEST_SELECT_XPATH="//div[@class='cdk-overlay-pane']//mat-option[last()]/span"
    FROM_ACC_SELECT_XPATH='//*[@id="select1"]'
    DESCRIPTION_TXT_XPATH='//*[@id="textarea-input"]'
    TRANSACTION_DATE_BUTTON_XPATH='//*[@id="transactionDate"]'
    DATE_SELECT_XPATH="//table//tr[1]/td/span[text()='1']"
    PAYABLE_AMOUNT_TXT_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-view-purchase-order-payments/div/div[2]/div/div[2]/form/div[6]/table/tbody/tr/td[9]/input"
    PAY_NOW_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-view-purchase-order-payments/div/div[2]/div/div[3]/div/button[1]"


    def __init__(self,driver):
        self.driver=driver

    def Click_Pay_PB(self):
        self.driver.find_element_by_xpath(self.PAY_PURCHASE_BILL_ITEM_XPATH).click()

    def Search_PO(self,po):
        self.driver.find_element_by_xpath(self.SEARCH_PO_LABEL_XPATH).click()
        self.driver.find_element_by_xpath(self.SEARCH_PO_TXT_XPATH).send_keys(po)
        element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.LATTEST_SELECT_XPATH)))
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def Add_data(self,BANK,DESC):
        sleep(5)
        select=Select(self.driver.find_element_by_xpath(self.FROM_ACC_SELECT_XPATH))
        select.select_by_visible_text(BANK)
        self.driver.find_element_by_xpath(self.DESCRIPTION_TXT_XPATH).send_keys(DESC)
        self.driver.find_element_by_xpath(self.TRANSACTION_DATE_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.DATE_SELECT_XPATH).click()

    def Amount(self,AMO):
        self.driver.find_element_by_xpath(self.PAYABLE_AMOUNT_TXT_XPATH).clear()
        self.driver.find_element_by_xpath(self.PAYABLE_AMOUNT_TXT_XPATH).send_keys(AMO)

    def Click_Pay_Now(self):
        self.driver.find_element_by_xpath(self.PAY_NOW_BUTTON_XPATH).click()



