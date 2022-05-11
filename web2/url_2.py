from urllib.error import HTTPError, URLError
from urllib import request
from html.parser import HTMLParser
import re

url = "https://stackoverflow.com/questions/33396785/how-to-find-a-particular-word-in-html-page-through-beautiful-soup-in-python"

user_input = input()
filename = user_input.split("/")[-1] + ".txt"

with request.urlopen(url) as f:
    data = f.read()
    with open(filename, "w") as out_file:
        decoded_data = data.decode(encoding = "utf-8", errors="strict")
        out_file.write(decoded_data)
        print("Written.")
