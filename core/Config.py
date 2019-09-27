class Config(object):
    """Config Loader
        srcInterfaceID = 'default'
        dstInterfaceID = 'default'
        dstFlowName = 'default'

    """


    def __init__(self, srcInterfaceID, dstInterfaceID, dstFlowName):
        """Return a flow object """         
        self.srcInterfaceID = srcInterfaceID
        self.dstInterfaceID = dstInterfaceID
        self.dstFlowName = dstFlowName
        #self.vf = vf
    

    def set_derived_val(self, vf,mf,fac):
        """Set the derived values, this will be computed from 
            input params
        """
        self.vf = vf
        self.mf = mf
        self.fac = fac

    def display(self):
        print("display constructer")
        print(self.srcInterfaceID,self.dstInterfaceID,self.dstFlowName)
        
        print(self.vf,self.mf,self.fac)

if __name__ == '__main__':
    print("Config called")