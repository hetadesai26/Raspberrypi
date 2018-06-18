from sense_hat import SenseHat 
sense = SenseHat() 
sense.clear() 
temp =sense.get_temperature()
print(temp)
sense.show_message(str(temp),text_colour=(255,0,0))
