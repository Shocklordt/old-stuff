import re
from urllib.request import urlopen

# counts the amount of matches
url = "https://en.wikipedia.org/wiki/Terrorism"

with urlopen(url) as f:
    r = f.read()
    decoded = r.decode("utf-8")
    dangerous_words = re.findall(r"\b(bomb|kill|murder|terror|terrorist|terrorists|terrorism)\b", decoded)
    print("The amount of dangerous words is: " + str(len(dangerous_words)))