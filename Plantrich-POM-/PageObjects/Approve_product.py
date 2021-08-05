from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class Approve_product:

    """PageObjectives"""
    CATALOG_MENUiTEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[3]/a"
    APPROVE_BUTTON_MENUITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[3]/app-sidebar-nav-items/app-sidebar-nav-link[5]/a"
    PAGE_COUNT_XPATH="//pagination-template/ul/li"
    NEXT_BUTTON_XPATH="//pagination-template/ul/li[last()]"
    LAST_RAW_ACTION_XPATH="//table//tr[last()]/td[last()]/div//*[name()='svg']"
    APPROVE_BUTTON_XPATH="//div/label[@class='btn btn-success'][1]"
    YES_APPROVE_XPATH="/html/body/modal-container/div/div/app-approval-confirmation/div/div[3]/button[1]"
    LATTEST_ID_XPATH="//table//tr[last()]/td[1]"



    def __init__(self,driver):
        self.driver=driver

    def Click_Catalog_Menuitem(self):
        self.driver.find_element_by_xpath(self.CATALOG_MENUiTEM_XPATH).click()

    def Click_Approve_Menuitem(self):
        sleep(2)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_BUTTON_MENUITEM_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Goto_last_page(self):
        sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Page_count = self.driver.find_elements_by_xpath(self.PAGE_COUNT_XPATH)
        num=len(Page_count)-3
        for i in range(num):
            sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.NEXT_BUTTON_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()

    def Click_Action_on_lattest(self):
        self.driver.find_element_by_xpath(self.LAST_RAW_ACTION_XPATH).click()

    def Click_Approve_button(self):
        sleep(1)
        self.driver.find_element_by_xpath(self.APPROVE_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.YES_APPROVE_XPATH).click()

    def Get_lattest_num(self):
        ID=self.driver.find_element_by_xpath(self.LATTEST_ID_XPATH).text
        return ID


