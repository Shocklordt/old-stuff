import re

# counts the amount of matches
text = "damn.txt"

with open(text, "r") as f:
    r = f.read() 
    dangerous_words = re.findall(r"\b(bomb|kill|murder|terror|terrorist|terrorists|terrorism|sunny)\b", r)
    print("The amount of dangerous words is: " + str(len(dangerous_words)))
