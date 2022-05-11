
def ask_float(s, error="Please enter a valid floating point number."):
    while True:
        try:
            return float(input(s))
        except ValueError:
            print(error)

inch = ask_float("How many inches?", "Invalid input")
cm = float(inch) * 2.54
print(f"{inch} inches in {cm} centimeters")


