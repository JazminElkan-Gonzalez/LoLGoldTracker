import pyscreenshot as ImageGrab
import subprocess
from PIL import *
from pytesser import *
import matplotlib.pyplot as plt


im = Image.open("TestImage.tif")
w, h = im.size
im.crop((w*15/112, h-h*3/100, w/6, h-h/150)).save("part.tif")
im2 = Image.open("part.tif")
(widths, heights) = im2.size
im2 = im2.resize((widths*3/2, heights*3/2), Image.ANTIALIAS)
im2.save("part.tif")