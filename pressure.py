from sense_hat import SenseHat 
sense = SenseHat() 
sense.clear() 
pressure= sense.get_pressure()
print(pressure)
sense.show_message(str(pressure),text_colour=(255,255,255))
