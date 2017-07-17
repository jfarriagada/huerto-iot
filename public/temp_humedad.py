import pyrebase
import RPi.GPIO as GPIO
import dht11
import datetime 

# config firebase
config = {
  "apiKey": "AIzaSyDzITeyDliMqldTwAivTm0pnY6O7m3vv3w",
  "authDomain": "huertoiot.firebaseapp.com",
  "databaseURL": "https://huertoiot.firebaseio.com",
  "storageBucket": "huertoiot.appspot.com"
}
firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin = 17)
result = instance.read()

if result.is_valid():
    # save data in firebase
    data = {
      "Temperature": result.temperature,
      "Humidity": result.humidity,
      "Timestamo" : str(datetime.datetime.now)
    }
    db.child("sensor").push(data)
    
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    print("Timestamp" % str(datetime.datetime.now))
else:
    print("Error: %d" % result.error_code)
