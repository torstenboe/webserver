from twython import Twython

C_KEY = "..."
C_SECRET = "..."
A_TOKEN = "..."
A_SECRET = "..."

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print("Found it!")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.status.filter(track="Harris")