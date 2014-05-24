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

LayerHasLayerCountNumber = 0;
LayerCount = 0;
ActualLayer = 0;
ActualObject=0;

with open(filename, "w") as f:
	for line in lines:
		if line.startswith(';LAYER:'):
			if LayerHasLayerCountNumber == 0:
				LayerHasLayerCountNumber = 1
				LayerCount = LayerCount + 1
		else:
			LayerHasLayerCountNumber = 0;
			
	LayerCount = str(LayerCount - 1)
	
	for line in lines:
		f.write(line)
		#print the actual layer
		if line.startswith(';LAYER:'):
			ActualLayer = getLayerNumber(line,None)
			#+1 because the LayerNumber starts with 0
			ActualLayer = int(ActualLayer)
			ActualLayer = ActualLayer + 1
			if ActualLayer <= int(LayerCount):
				ActualLayer = str(ActualLayer)
				f.write("M117 Layer " + ActualLayer + " of " + LayerCount + ".\n")
			
		
