import unittest

from core.Config import Config
from core.Flows import FlowType,PatternType,Flows


class Test(unittest.TestCase):

    def setUp(self):
        ##data init
        print("Start test...")
        self.cfgdict = {'srcInterfaceID': 'MSF21ADT', 'dstInterfaceID': 'AMPSTC21ADT', 'dstFlowName': 'CIM_2_NSTMMC21_AMPSTCADT', 'vf': 'NSTMMC21_MSFADT_VALID_2_MAP', 'mf': 'NSTMMC21_MSFADT_MAP_2_CIM', 'fac': 'NSTMMC21'}
        self.flowdict =  {'name': 'CIM_2_NSTMMC21_AMPSTCADT', 'flowType': FlowType.VF, 'config': self.cfgdict, 'patternType': PatternType.AMP}

    def test_config(self):
        """
        Test Config object
        """
        print("Start test of Config class...")
        c = Config('MSF21ADT','AMPSTC21ADT','CIM_2_NSTMMC21_AMPSTCADT')
        c.set_derived_val('NSTMMC21_MSFADT_VALID_2_MAP','NSTMMC21_MSFADT_MAP_2_CIM','NSTMMC21')
        data = vars(c)
        result = len(data)
        self.assertEqual(result, 6)
        self.assertDictEqual(data,self.cfgdict)

    def test_flows(self):
        """
        Test Flows object
        """
        print("Start test of Flows class...")
        c = Config('MSF21ADT','AMPSTC21ADT','CIM_2_NSTMMC21_AMPSTCADT')
        c.set_derived_val('NSTMMC21_MSFADT_VALID_2_MAP','NSTMMC21_MSFADT_MAP_2_CIM','NSTMMC21')
        flow = Flows(c.dstFlowName,FlowType.VF,vars(c),patternType=PatternType.AMP)
        data = vars(flow)
        #result = len(data)
        #self.assertEqual(result, 6)
        self.assertDictEqual(data,self.flowdict)

if __name__ == '__main__':
    unittest.main()