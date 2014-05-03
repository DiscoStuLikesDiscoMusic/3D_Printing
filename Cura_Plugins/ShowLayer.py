#Name: ShowLayer
#Info: Shows the actual layer on the Ulticontroller
#Depend: GCode
#Type: postprocess

__copyright__ = "Copyright (C) 2013 Dominic von Bergen - Released under terms of the AGPLv3 License"
import re

def getLayerNumber(line, default = None):
	number = 0;
	#Remove Carrage Return in String
	line = line.replace("\n", "")
	#Extract number
	number =  line.split(':')[1]
	
	if number is None:
		return default
	try:
		return number
	except:
		return default

with open(filename, "r") as f:
	lines = f.readlines()

NumberOfLayer = 0;
ActualLayer=0;
NumberOfObjects=0;
ActualObject=0;

with open(filename, "w") as f:
	for line in lines:
		f.write(line)
		#Get the whole count of layer
		if line.startswith(';Layer count:'):
			NumberOfObjects = NumberOfObjects+1
			NumberOfLayer = getLayerNumber(line,None)
			NumberOfLayer = str(NumberOfLayer)
		#print the actual layer
		if line.startswith(';LAYER:'):
			ActualLayer = getLayerNumber(line,None)
			#+1 because the LayerNumber starts with 0
			ActualLayer = int(ActualLayer)
			ActualLayer = ActualLayer+1
			ActualLayer = str(ActualLayer)
			f.write("M117 Layer " + ActualLayer + " of" + NumberOfLayer + "\n")
