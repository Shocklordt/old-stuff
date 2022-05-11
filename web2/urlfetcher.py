from ntpath import join
from urllib import request, error
from html.parser import HTMLParser
from re import findall
from os import path
from sys import exit

all_data = []

class myHTMLParser(HTMLParser):
    def handle_data(self, data):
        global all_data
        all_data.append(data)

def fetch_url():
    user_url = input("Please enter a valid url: ")
    try:
        # Opens the URL
        with request.urlopen(user_url) as f:
            # Tries to read, decode and parse. 
            # On success: appends all the items to a list, then creates a new string out of all the elements.
            # On fail: Tries to download the contents of a URL to a specified path.
            try:
                parser = myHTMLParser()
                r = f.read().decode("utf-8")
                s = parser.feed(r)
                string = " ".join([str(item) for item in all_data])
                dangerous_words = findall(r"\b(bomb|kill|murder|terror|terrorist|terrorists|terrorism)\b", string)
                print("The amount of dangerous words is: " + str(len(dangerous_words)))
                all_data.clear()

                user_path = input("Attempting to download url. Please enter a valid path: ")
                filename = path.join(user_path)
                request.urlretrieve(user_url, filename)
                print("File written.")
                exit()

            except ValueError:
                print("Does not appear to be an HTML file with UTF-encoding. Attempting to download...")
                user_path = input("Please enter a valid path: ")
                filename = path.join(user_path)
                request.urlretrieve(user_url, filename)
                print("File written.")
                exit()
                    
    except error.URLError:
        print("Error opening URL")
    except ValueError:
        print("Invalid URL")
    except KeyboardInterrupt:
        print("Invalid keyboard command, please try again. ")
    except OSError:
        print("Invalid path. Download failed.")

def Main():
    Quit = False
    while Quit == False:
        fetch_url()
    else:
        Quit = True
Main()