from .Config import Config
from enum import Enum

class FlowType(Enum):
    VF = 1
    MF = 2 
    DF = 3

#FlowType = Enum('FlowType', 'VF MF DF')
PatternType = Enum('PatternType', 'CXN AMP')

__all__ = ['FlowType','PatternType','Flows']

class Flows(object):
    """Abstract class to represent flows. Flows have the
    following properties:

    Attributes:
        name: A string representing the name.
        flowType: Enum for type of flow - vf, mf or df
        patternType: Enum for type of design pattern - cxn or amp
        config = {} : dictionary of common configuration properties
    """
    

    def __init__(self, name, flowType:FlowType, config:Config, patternType:PatternType = 'AMP'):
        """Return a flow object """         
        self.name = name
        self.flowType = flowType
        self.config = config
        self.patternType = patternType


    def generate(self, name):
        """Generate the appropriate flow

        """


    def validate(self, name):
        """validate the flow
        """
       