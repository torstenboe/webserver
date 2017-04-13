from twython import Twython
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

C_KEY = "..."
C_SECRET = "..."
A_TOKEN = "..."
A_SECRET = "..."

def blink():
    GPIO.output(13, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(13, GPIO.LOW)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print("Found it!")
            blink()

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.status.filter(track="Harris")