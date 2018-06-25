import requests
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True

apiKey = "b3fe6747149f555862b090f9cb737f51"

temp = 0
minTemp = 0
maxTemp = 0
humidity = 0

def getWeatherData():
    global temp
    global minTemp
    global maxTemp
    global humidity
    global currentCity
    
    url = ("http://api.openweathermap.org/data/2.5/weather?"
           "q=new+york&appid="+apiKey+"&units=metric")
    r = requests.get(url)
    data = r.json()

    currentCity = data["name"]
    temp = data["main"]["temp"]
    minTemp = data["main"]["temp_min"]
    maxTemp = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]
    print(currentCity)
    print(temp)
    print(minTemp)
    print(maxTemp)
    print(humidity)
    
    sense.show_message(str(temp),scroll_speed=0.3)
    sense.show_message(str(minTemp),scroll_speed=0.3)   
    sense.show_message(str(maxTemp),scroll_speed=0.3)
    sense.show_message(str(humidity),scroll_speed=0.3)


getWeatherData()
