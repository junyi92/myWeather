# ===========
# weather.py 
# ===========
from urllib.request import urlopen
import json
import sys

#http://api.openweathermap.org/data/2.5/weather?q=OSLO&appid=3f63ccf4a308a813a06606c1bc526a16
def get_weather(city):
    sock = urlopen("https://api.openweathermap.org/data/2.5/weather?q="; + 
                   city + "&appid=6f0bfb3232d4642285811d8fbe3fc9a8")
    result = sock.read()
    sock.close()
    weather = json.loads(result)
    return weather["main"]["temp"] - 273.15

def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/"+postal_code)
    result = sock.read()
    sock.close()
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longitude"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        city = sys.argv[1]
    else:
        city = "OSLO"
    
    degrees = get_weather(city)
    print(f"Weather in {city} in {degrees:.2f} degree celcius.")
    postal = "OX12JD"  #UK postal code
    location = postal_lookup(postal)
    print(f"Postal code {postal} is at location {location}")
