from twython import TwythonStreamer

C_KEY = "..."
C_SECRET = "..."
A_TOKEN = "..."
A_SECRET = "..."

count = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if ('text' in data) && (count < 3):
            count += count
            print("found")
        else if ('text' in data) && (count == 3):
            count = 0
            print("Ian G. Harris is popular!")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.status.filter(track="Ian G. Harris")