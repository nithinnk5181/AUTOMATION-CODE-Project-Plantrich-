from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class ApproveRequisition:
    '''PageObjectives'''
    APPROVE_REQUISITION_BUTTON_XPATH="/html/body/app-root/app-dashboard/div/app-sidebar/app-sidebar-nav/app-sidebar-nav-items/app-sidebar-nav-dropdown[4]/app-sidebar-nav-items/app-sidebar-nav-link[3]/a/app-sidebar-nav-link-content"
    APPROVE_REQUISITION_ACTION_BUTTON_XPATH="//table[@class='table table-striped']/tbody/tr[1]/td[last()]/div/div/*[name()='svg']"
    ACCEPT_BUTTON_XPATH="//div/label[@class='btn btn-success']"
    DECLINE_BUTTON_XPATH="//div/label[@class='btn btn-danger']"
    APPROVE_YES_BUTTON_POPUP_XPATH="/html/body/modal-container/div/div/app-approval-confirmation/div/div[3]/button[1]"
    DECLINE_YES_BUTTON_POPUP_XPATH="/html/body/modal-container/div/div/app-decline-confirmation/div/div[3]/button[1]"
    FIRST_ROW_REQUISITION_NUMBER_XPATH="//table[@class='table table-striped']/tbody/tr[1]/td[1]"

    def __init__(self,driver):
        self.driver=driver

    def click_Approve_Requisition(self):
        self.driver.find_element_by_xpath(self.APPROVE_REQUISITION_BUTTON_XPATH).click()

    def click_Approve_Req_Button(self):
        element=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_REQUISITION_ACTION_BUTTON_XPATH)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click().perform()

    def click_Approve_Button(self):
        sleep(1)
        try:
            #Javascript click
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.ACCEPT_BUTTON_XPATH)))
            self.driver.execute_script("arguments[0].click();", element)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPROVE_YES_BUTTON_POPUP_XPATH))).click()
        except:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ACCEPT_BUTTON_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()

    def click_Decline_Button(self):
        sleep(1)
        try:
            ##Javascript click
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.DECLINE_BUTTON_XPATH)))
            self.driver.execute_script("arguments[0].click();",element)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLINE_YES_BUTTON_POPUP_XPATH))).click()
        except:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.DECLINE_BUTTON_XPATH)))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            actions.click().perform()

    def get_table_data(self):
        column=self.driver.find_element_by_xpath(self.FIRST_ROW_REQUISITION_NUMBER_XPATH)
        return column.text




