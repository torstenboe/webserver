from twython import TwythonStreamer

C_KEY="..."
C_SECRET="..."
A_TOKEN="..."
A_SECRET="..."

count = 1

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global count
        if ('text' in data) and (count < 3):
            count = count + 1
        elif ('text' in data) and (count <= 3):
            print("Ian G. Harris is popular!")

stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)

stream.statuses.filter(track="Ian G. Harris")