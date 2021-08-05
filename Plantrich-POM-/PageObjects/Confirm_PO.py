from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Confirm_PO:
    """Page Objectives"""
    CONFIRM_PO_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[5]/app-sidebar-nav-items/app-sidebar-nav-link[3]/a/app-sidebar-nav-link-content"
    CONFIRM_ACTION_LATEST_PO_XPATH="//table/tbody/tr[1]/td[last()]/div/div"
    APPROVE_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-confirm-purchase-order-action/div/div[2]/div/div[1]/div[2]/div[2]/div/label[1]"
    DECLAIN_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/main/div/app-confirm-purchase-order-action/div/div[2]/div/div[1]/div[2]/div[2]/div/label[2]"
    APPROVE_CONFIRM_YES_XPATH="/html/body/modal-container/div/div/app-approval-confirmation/div/div[3]/button[1]"
    DECLAIN_CONFIRM_YES_XPATH="/html/body/modal-container/div/div/app-decline-confirmation/div/div[3]/button[1]"
    LATTEST_PO_NUMBER="//table/tbody/tr[1]/td[1]"


    def __init__(self,driver):
        self.driver=driver

    def Click_confirm_PO_item(self):
        self.driver.find_element_by_xpath(self.CONFIRM_PO_ITEM_XPATH).click()

    def Click_Action_lattest_PO(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CONFIRM_ACTION_LATEST_PO_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Click_Approve_button(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_BUTTON_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Click_Declain_button(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLAIN_BUTTON_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Click_Approve_Confirm_yes(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_CONFIRM_YES_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Click_Declain_Confirm_yes(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLAIN_CONFIRM_YES_XPATH)))
        self.driver.execute_script("arguments[0].click();", element)

    def Get_lattest_PO_number(self):
        PO_num=self.driver.find_element_by_xpath(self.LATTEST_PO_NUMBER).text
        return PO_num
