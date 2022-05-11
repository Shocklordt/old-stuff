names = ["Jack", "Bob", "Alice", "Bill", "Jane", "Zack"]

print("Original order:")
for name in names:
    print(name)

print("Alphabetical order:")
names.sort()
for name in names:
    print(name)

print("Reverse order:")
for name in reversed(names):
    print(name)

print(names)

