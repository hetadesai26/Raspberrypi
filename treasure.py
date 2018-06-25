from sense_hat import SenseHat
from random import randint
from time import sleep
sense=SenseHat()
score=0
play=True
x=0
y=0
px=0
py=0
def draw():
	global x,y,px,py
	sense.clear()
	x=randint(0,7)
	y=randint(0,7)
	sense.set_pixel(x,y,(0,0,255))
	sleep(2)
	sense.clear()
	sleep(2)
        px=0
        py=0
        sense.set_pixel(0,0,(255,0,255))
			
while play:
	draw()
	while True:
		 for e in sense.stick.get_events():
			if e.action=="pressed":
				sense.clear()
				print("inside")	
      				if e.direction == "up":
        				if py==0:
						py=7
					else:
						py=py-1
					print(py)
					sense.set_pixel(px,py,(255,255,255))
      				elif e.direction == "down":
        				if py==7:
						py=0
					else:
						py=py+1
					sense.set_pixel(px,py,(255,255,255))
      				elif e.direction == "left": 
        				if px==0:
						px=7
					else:
						px=px-1
					sense.set_pixel(px,py,(255,255,255))
      				elif e.direction == "right":
        				if px==7:
						px=0
					else:
						px=px+1
					sense.set_pixel(px,py,(255,255,255))
				elif e.direction == "middle":
                                	if px==x and py==y:
                                        	sense.set_pixel(x,y,(0,255,0))
						sleep(1)
                                        	score=score+1
						draw()
						break
                                	else:
                                        	play=False
                                        	sense.set_pixel(x,y,(255,0,0))
						sleep(1)
						sense.show_message("game over")
                                        	str="Score:"+str(score)
                                        	sense.show_message(str)
                                        	exit()

			else:
				print("out")
			
		
      			      
      			
sense.clear()	
	
