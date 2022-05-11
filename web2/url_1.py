from fileinput import filename
from urllib.error import HTTPError, URLError
from urllib import request
from html.parser import HTMLParser
import re


def Main():
    Quit = False
    while Quit == False:
            print("Please enter a valid url: ")
            user_input = input()
            filename = user_input.split("/")[-1]
            path_input = input("Please enter a valid path: ")

            def downloadBinary():
                try:
                    request.urlretrieve(user_input, filename)
                except URLError:
                    pass
            
            def downloadHTML():
                try:
                    with open(filename, "w") as out_file:
                        decoded_data = data.decode("utf-8")
                        out_file.write(decoded_data)
                        print("data written to data.html")
                except HTTPError:
                    print("Error opening URL")
                    pass

            try:
                with request.urlopen(user_input) as f:
                    data = f.read()
                    
                    if user_input.endswith(".png" or ".jpg" or ".gif"):
                        downloadBinary()
                    
                    elif user_input.endswith(".html"):
                        
                            
                    else:
                        continue

            except ValueError:
                print("Invalid URL")
            except URLError:
                print("Invalid URL")
            except OSError:
                print("Error writing file.")
Main()
