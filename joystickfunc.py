from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

 
def red(): 
	sense.clear(255,0,0)
	return
def blue():
	sense.clear(0,0,255)
def yellow():
	sense.clear(0,255,255)
def green():
	sense.clear(0,255,0) 
while True:
	sense.stick.direction_up = red 
	sense.stick.direction_down = blue
	sense.stick.direction_left = green 
	sense.stick.direction_right = yellow 

  
def yellow():
  sense.clear(255, 255, 0)
