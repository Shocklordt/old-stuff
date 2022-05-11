from html.parser import HTMLParser
import re
from urllib.request import urlopen

class myHTMLParser(HTMLParser):
    def handle_data(self, data):
        global all_data
        all_data.append(data)
        

parser = myHTMLParser()
url = "https://en.wikipedia.org/wiki/Terrorism"
url2 = "https://fi.wikipedia.org/wiki/Bomban_talo"

all_data = []

with urlopen(url) as f:
    r = f.read().decode("utf-8")
    s = parser.feed(r)

string = " ".join([str(item) for item in all_data])
dangerous_words = re.findall(r"\b(bomb|kill|murder|terror|terrorist|terrorists|terrorism)\b", string)
print("The amount of dangerous words is: " + str(len(dangerous_words)))