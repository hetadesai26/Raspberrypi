from sense_hat import SenseHat 
sense = SenseHat() 
sense.clear() 
humidity = sense.get_humidity()
print(humidity)
sense.show_message(str(humidity)+"h",text_colour=(0,0,255))
