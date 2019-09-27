from core import Config
class Generator(object):
    """Generator util class
    Attributes:
    config:  config loader object
    """


    def __init__(self, config:Config):
        """Return a flow object """         
        self.config = config


    

    def generate(self):
        """Set the derived values, this will be computed from 
            input params
        """



