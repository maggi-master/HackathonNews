import numpy as np

class Tag:
    def __init__(self, tag:str):
        self.tag = tag
        self.vector:np.ndarray = None
