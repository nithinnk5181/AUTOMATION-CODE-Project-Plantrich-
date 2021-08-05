from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


class Generate_purchase_bill:
    """PageObejctives"""
    GENERATE_PURCHASE_BILL_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[5]/app-sidebar-nav-items/app-sidebar-nav-link[6]/a/app-sidebar-nav-link-content"
    ACTION_LATTEST_ITEM_XPATH="//table//tr[1]/td[last()]//*[name()='svg']"
    LATTEST_PO_ID_XPATH="//table//tr[1]/td[1]"
    GENERATE_BILL_BUTTON_XPATH="//label[@class='btn btn-success']"

    def __init__(self,driver):
        self.driver=driver

    def Click_on_Generate_PB(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.GENERATE_PURCHASE_BILL_ITEM_XPATH)))
        element.click()

    def Click_on_Action(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ACTION_LATTEST_ITEM_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Click_on_GenerateButton(self):
        sleep(2)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.GENERATE_BILL_BUTTON_XPATH)))
        element.click()

    def Get_lattest_id(self):
        id=self.driver.find_element_by_xpath(self.LATTEST_PO_ID_XPATH).text
        return id
