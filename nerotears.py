# By Raynard Jon
# raynard@rasenn.com
# Show shiny liquid on your sense hat 8*8 matrix
# Run the code and try to move around the rpi
from sense_hat import SenseHat
import numpy as np
sense=SenseHat()
# Turn 90 degrees
# If angle still not right on your rpi
# Try more degrees
sense.set_rotation(90)
# Raw scall
raw=(np.array(range(8),dtype=np.float)-3.5)/4
pix=[]
while True:
	# Orientation Degree
	o_deg = sense.get_orientation()
	# Degree of Pitch
	dp=o_deg["pitch"]
	# Degree of Roll
	dr=o_deg["roll"]
	# Adjust Value to balance around zero
	if dp>180: dp-=360
	if dr>180: dr-=360
	# Adjust the scale
	pitch=raw*(dp)*15/18
	roll=raw*(dr)*15/18
	#print "%s,%s"%(pitch,roll)
	for p in range(8):
		for r in range(8):
			# add up pitch and roll array spot
			# Make sure it's larger than 0
			v=max(int(50+pitch[p]+roll[r]),0)
			# Set colors of a pixel
			# Tone down the RED and GREEN
			# To give a blue quality
			c=[int(v*0.8),int(v*0.8),v]
			pix.append(c)
	sense.set_pixels(pix)
	pix=list()