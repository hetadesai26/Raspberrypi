from sense_hat import SenseHat
from random import randint

ran_red=randint(0,255)
ran_blue=randint(0,255)
ran_green=randint(0,255)

sense=SenseHat()

sense.show_message("Hi",text_colour=(ran_red,ran_green,ran_blue))


