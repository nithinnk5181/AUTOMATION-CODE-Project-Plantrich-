from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class Approve_storage:
    """PageObjectived"""
    MATERIAL_STORAGE_MENUITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[7]/a"
    APPROVE_STORAGE_ITEM_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[7]/app-sidebar-nav-items/app-sidebar-nav-link[3]/a/app-sidebar-nav-link-content"
    ACTION_LATTEST='//table//tr[1]/td[last()]/div/div/*[name()="svg"]'
    LATTEST_MS_NUMBER="//table//tr[1]/td[1]"
    APPROVE_BUTTON_XPATH="//div/div/button[1]"
    DECLAIN_BUTTON_XPATH="//div/div/button[2]"
    APPROVE_YES_XPATH="/html/body/modal-container/div/div/app-approval-confirmation/div/div[3]/button[1]"
    DECLAIN_YES_XPATH="/html/body/modal-container/div/div/app-decline-confirmation/div/div[3]/button[1]"


    def __init__(self,driver):
        self.driver=driver

    def click_Approve_storage(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.MATERIAL_STORAGE_MENUITEM_XPATH).click()
        sleep(3)
        self.driver.find_element_by_xpath(self.APPROVE_STORAGE_ITEM_XPATH).click()

    def Click_action(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ACTION_LATTEST)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def Approve(self):
        sleep(2)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_BUTTON_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        self.driver.find_element_by_xpath(self.APPROVE_YES_XPATH).click()

    def Declain(self):
        sleep(2)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLAIN_BUTTON_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()
        self.driver.find_element_by_xpath(self.DECLAIN_YES_XPATH).click()

    def Get_lattest_id(self):
        sleep(5)
        id = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, self.LATTEST_MS_NUMBER)))
        return id

