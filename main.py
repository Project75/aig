from core.Config import Config
from core.Flows import FlowType,PatternType,Flows

c = Config('MSF21ADT','AMPSTC21ADT','CIM_2_NSTMMC21_AMPSTCADT')
c.set_derived_val('NSTMMC21_MSFADT_VALID_2_MAP','NSTMMC21_MSFADT_MAP_2_CIM','NSTMMC21')
#c.display()
print(" - Config Vars   - ")
print(vars(c))

flow = Flows(c.dstFlowName,FlowType.VF,vars(c),patternType=PatternType.AMP)
print(" - Flow Vars   - ")
print(vars(flow))