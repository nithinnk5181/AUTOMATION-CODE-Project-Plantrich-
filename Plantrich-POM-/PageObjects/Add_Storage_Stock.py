from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class Add_stock:
    """PageObjectives"""
    MATERIAL_STORAGE_MENUITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[7]/a"
    ADD_STORAGE_STOCK_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[7]/app-sidebar-nav-items/app-sidebar-nav-link[5]/a/app-sidebar-nav-link-content"
    ACTION_LATEST_ITEM_XPATH="//table//tr[1]/td[last()]//*[name()='svg']"
    LATTEST_ITEM_ID="//table//tr[1]/td[1]"
    ADD_TO_STOCK_BUTTON_XPATH="//div/button[1]"
    YES_BUTTON_XPATH="/html/body/modal-container/div/div/app-approval-confirmation/div/div[3]/button[1]"

    def __init__(self,driver):
        self.driver=driver

    def Click_add_to_stock(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.MATERIAL_STORAGE_MENUITEM_XPATH).click()
        sleep(2)
        self.driver.find_element_by_xpath(self.ADD_STORAGE_STOCK_ITEM_XPATH).click()

    def Click_Action_lattest(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ACTION_LATEST_ITEM_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Click_add_to_stock_button(self):
        sleep(2)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ADD_TO_STOCK_BUTTON_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        self.driver.find_element_by_xpath(self.YES_BUTTON_XPATH).click()

    def Get_lattest_id(self):
        id=self.driver.find_element_by_xpath(self.LATTEST_ITEM_ID).text
        return id


