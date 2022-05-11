import json

# Dictionary
# Saves to JSON.
# Adds new words.
# Finds words and its translations.
# Error catching.
# Adds new words if not found.
# Creates a JSON file if it doesnt exist.
# encoding in utf-8


# Converts JSON to python dictionary and prints it out
def print_items():
    try:
        with open("dict.json", "r", encoding="utf8") as f:
            dict_out = json.load(f)
            for key, value in dict_out.items():
                print(key, value, sep = " = ")

    except json.JSONDecodeError:
        pass

    except OSError:
        print("No content to print. Adding default dictionary.")
        default_d = {"word" : "translation"}
        with open("dict.json", "w", encoding="utf8") as f:
            json.dump(default_d, f)
            return


# Adds a new word and its translation to the dictionary.
def add_item():

    dict = {"word" : "translation"}
    print("Enter the word")
    add_word = input()

    print("Enter the translation")
    add_t = input()
    dict[add_word] = add_t

    try:
        with open("dict.json", "r", encoding="utf8") as s:
            dict_s = json.load(s)
            dict.update(dict_s)

    except json.JSONDecodeError:
        pass

    except OSError:
        print("No content to print. Adding default dictionary.")
        with open("dict.json", "w", encoding="utf8") as f:
            json.dump(dict, f)
            f.close()
            print("Added " + add_word + " and " + add_t + " to the dictionary ")
            return

    try:
        with open("dict.json", "w", encoding="utf8") as f:
            json.dump(dict, f)
            f.close()
            print("Added " + add_word + " and " + add_t + " to the dictionary ")
            return

    except json.JSONDecodeError:
        pass

# Searches for items in dictionary and runs add_item() if the item [key or value] are not a searched item
def search_item():
    print("Enter the word you would like to find: ")
    searched_item = input()
    try:
        with open("dict.json", "r", encoding="utf8") as f:
            dict_out = json.load(f)
            for key in dict_out.keys():
                if key == searched_item:
                    print(key, dict_out[key], sep=" = ")
                    return

                elif key is not searched_item:
                    for key, value in dict_out.items():
                        if value == searched_item: 
                            print(key, value, sep = " = ")
                            return
            else:
                print("Item not found, lets add it")
                add_item()

    except json.JSONDecodeError:
        pass

    except OSError:
        print("No content to print. Adding default dictionary. Please try again.")
        default_d = {"word" : "translation"}
        with open("dict.json", "w", encoding="utf8") as f:
            json.dump(default_d, f)
            return

# Main loop
def Main():

    Quit = False
    while Quit == False:
        print("Welcome to the dictionary! Press 1 to print it. Press 2 to add a word to the dictionary. Press 3 to search for a word.")
        user_input = input()

        if user_input == "1":
            print_items()

        elif user_input == "2":
            add_item()

        elif user_input == "3":
            search_item()

        elif user_input == {"q" or "quit" or "e" or "exit" or ""}:
            print("Goodbye !")
            Quit = True

        else:
            Quit = True
Main()