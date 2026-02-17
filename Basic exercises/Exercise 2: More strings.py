text = "  Hello, World! Welcome to Python Programming.  "
text2 = text.strip()
print("Stripped:", text2)
print("Words: ", len(text.split()))
print("Title:", text.title())
print("Starts with Hello: ", text2.startswith("Hello"))
print("Ends with ing.:", text2.endswith("ing."))
print("Python position: ", text2.find("Python"))
print("Joined", "-".join(text.strip().split()))