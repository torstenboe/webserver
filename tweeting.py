from twython import TwythonStream

C_KEY = "..."
C_SECRET = "..."
A_TOKEN = "..."
A_SECRET = "..."

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print("Ian G. Harris is popular!")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.status.filter(track="Ian G. Harris")