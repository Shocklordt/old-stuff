with open ("test.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2 ÄÖ\n")
print("File written")