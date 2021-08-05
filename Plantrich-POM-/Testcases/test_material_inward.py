#  pytest -v -s --html=Reports/test_material_inward.html --self-contained-html Testcases/test_material_inward.py --browser Firefox
#  pytest -v -s Testcases/test_material_inward.py --browser Firefox
#  pytest -v -s Testcases/test_material_inward.py --browser Chrome

from PageObjects.LoginPage import Login
from PageObjects.Create_Requisition import CreateRequisition
from PageObjects.Material_inward import Material_inward
from Prerequirments.Prerequirments import PREREQUIRMENTS
from Utilities.readproperties import ReadConfig
import pytest

BASEURL=ReadConfig.getBaseuRL()

class Test_001_Create_Material_inward:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=19)
    def test_Create_Material_inward(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.mi=Material_inward(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.mi.Click_material_inward()
        except:
            self.cr.Click_MenuIcon()
            self.mi.Click_material_inward()
        lattest_created_id=self.mi.get_LAST_CREATED_MATERIAL_INWARD_ID()
        self.mi.Click_Create_material_inward_button()
        self.mi.Serach_by_PO_num("PURCHASE-")
        self.mi.Select_lattest_PO()
        self.mi.Add_product1_details("test","123","50")
        self.mi.Add_product2_details("Test","321","30")
        self.mi.Add_basic_details("8086564523","Test","ware1")
        self.mi.Add_Checklist_details()
        self.mi.Click_save()#Save and submit

        lattest_updated_id = self.mi.get_LAST_CREATED_MATERIAL_INWARD_ID()
        if lattest_updated_id==lattest_created_id:
            # To take the Screenshote
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        else:
            self.driver.close()
            assert True



class Test_002_Create_Material_inward:


    @pytest.mark.regression
    @pytest.mark.run(order=20)
    def test_Create_Material_inward_failure(self,setup):

        """PREREQUIRMENTS"""


        """TESTCASE STARTS HERE"""


        self.driver=setup
        self.driver.get(BASEURL)
        # Classobject
        self.lp = Login(self.driver)#classObject
        self.cr = CreateRequisition(self.driver)
        self.mi=Material_inward(self.driver)


        # Login
        self.lp.login()

        #CreatePurchase Order
        try:
            self.mi.Click_material_inward()
        except:
            self.cr.Click_MenuIcon()
            self.mi.Click_material_inward()
        lattest_created_id=self.mi.get_LAST_CREATED_MATERIAL_INWARD_ID()
        self.mi.Click_Create_material_inward_button()
        self.mi.Serach_by_PO_num("PURCHASE-")
        self.mi.Select_lattest_PO()
        try:
            self.mi.Click_save()#Save and submit
            PREREQUIRMENTS.TAKE_SCREENSHOTE(self)
            assert False
        except:
            self.driver.close()
            assert True






