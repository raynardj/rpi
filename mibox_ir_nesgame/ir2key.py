
import serial as sl
import time
import datetime  

ser = sl.Serial('/dev/cu.usbmodem144201',9600) # or find your device in /dev


from pynput.keyboard import Key, Controller
k = Controller()

def press(x,sleep=None):
	k.press(x)
	if sleep !=None:
		time.sleep(sleep)
	k.release(x)

hexmap = {
	"EA58E625":["s","down"],
	"DE3AA631":["d","right"],
	"69893291":["w","up"],
	"6212287":["a","left"],
	"76A77416":["o","A"],
	"77A775AB":["o","A"],
	"8453B5A5":["p","B"],
	"F874E0F8":[Key.space,"option"],
	"EB58E7B6":[Key.enter,"select"],
}

def translator(x):
	x = str(x.decode("utf8")).strip()
	try:
		pair = hexmap[x]
		print(pair[1])
		press(pair[0], sleep=0.03)
	except:
		print(str(x))


while True: # Run loop indefinitely    
	translator(ser.readline())