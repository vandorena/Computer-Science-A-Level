import math

class boatproperties:
    def __init__(self,boattype):
        self._boattype = boattype
        if self._boattype == "Plane":
            
            if self._boattype == "foiling":
    
    def initfoil(self,breadthofsail,chordoffoil,weighttotal):
        self.breadthofsail = breadthofsail
        self.chordoffoil = chordoffoil
        self.weight = weighttotal
        self.g = 9.81
        return
        