import requests
from sense_hat import SenseHat 
sense = SenseHat() 
sense.clear()
apikey="b3fe6747149f555862b090f9cb737f51"
def getWeatherData():
    url = ("http://api.openweathermap.org/data/2.5/weather?"
           "q=new+york&appid="+apikey+"&units=metric")
    r = requests.get(url)
    data = r.json()
    print(data)
    
getWeatherData() 

