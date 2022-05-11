d = {"cat": "kissa", "dog": "koira"}

while True:
    word = input("Give me a word?")

    if not word: break

    if word in d:
        print(f"{word} = {d[word]}")
    
    else:
        definition = input(f"Word not found. Please give a definition for {word}?")
        if definition:
            d[word] = definition