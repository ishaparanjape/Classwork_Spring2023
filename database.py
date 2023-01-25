print("This is the database.py file")
print("Python thinks this is called {}".format(__name__))

#imports file and all of its functions
#from blood_calculator import *
import blood_calculator as bc
from blooc_calculator import HDL_analysis

HDL = 55
HDL_analysis = HDL_analysis(HDL)
print("The HDL analysis is {}".format(HDL_analysis))

bc.generic_input("Other Test")
print(LDL_analysis(13))

