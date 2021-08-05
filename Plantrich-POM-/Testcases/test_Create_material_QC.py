#  pytest -v -s --html=Reports/test_Create_material_QC.html --self-contained-html Testcases/test_Create_material_QC.py --browser Firefox
#  pytest -v -s Testcases/test_Create_material_QC.py --browser Firefox
#  pytest -v -s Testcases/test_Create_material_QC.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Create_material_QC import Material_QC
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Create_Material_QC:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=22)
    def test_Create_Material_QC(self,setup):

        """PREREQUIRMENTS"""
        #PREREQUIRMENTS.CREATE_MATERIAL_INWARD(self,setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.mq = Material_QC(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.mq.Click_on_Material_qc()
        except:
            self.cr.Click_MenuIcon()
            self.mq.Click_on_Material_qc()
        self.mq.Click_on_Create_Material_qc()
        self.mq.Click_on_SearchBox('MIR-')
        self.mq.Select_lattest_MIR()
        self.mq.Prod1_action()
        self.mq.Add_data("test","20")
        self.mq.Approve_QC()

        self.mq.Prod2_action()
        self.mq.Add_data("TEST","30")
        self.mq.Approve_QC()

        self.mq.Prod2_action()
        Present=self.mq.Check_PrintButton()

        if Present==True:
            assert True
            self.driver.close()
        else:
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False



class Test_002_Create_Material_QC:

    @pytest.mark.regression
    @pytest.mark.run(order=21)
    def test_Create_Material_QC_Fail(self,setup):

        """PREREQUIRMENTS"""
        #PREREQUIRMENTS.CREATE_MATERIAL_INWARD(self,setup)

        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.mq = Material_QC(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.mq.Click_on_Material_qc()
        except:
            self.cr.Click_MenuIcon()
            self.mq.Click_on_Material_qc()
        self.mq.Click_on_Create_Material_qc()
        self.mq.Click_on_SearchBox('MIR-')
        self.mq.Select_lattest_MIR()
        self.mq.Prod1_action()
        self.mq.Approve_QC()
        try:
            self.mq.Prod2_action()
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            assert True
            self.driver.close()

