import pyscreenshot as ImageGrab
import subprocess
from PIL import *
from pytesser import *
import matplotlib.pyplot as plt

def doneChecker():
	everything = subprocess.check_output(['tasklist', '/fo', 'csv'])
	everything = everything.replace('\"', "")
	everything = everything.split(",")
	for line in everything:
		if 'League of Legends.exe'in line:
			return True
			hasStarted = True
		elif line == everything[-1]:
			return False

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
  

hasStarted = False
goldList = []
while doneChecker():
	im = ImageGrab.grab()
	w, h = im.size
	im.crop((w*15/112, h-h*3/100, w/6, h-h/150)).save("part.tif")
	im2 = Image.open("part.tif")
	(widths, heights) = im2.size
	im2 = im2.resize((widths*3/2, heights*3/2), Image.ANTIALIAS)
	text = image_to_string(im2)
	if (is_number(text)):
		goldList.append(int(text))
print(goldList)
plt.plot(goldList)
plt.ylabel("gold")
plt.show()