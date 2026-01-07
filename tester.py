import re

pattern = input("Enter regex pattern: ")
text = input("Enter text: ")

matches = re.findall(pattern, text)

if matches:
    print("Matches found:", matches)
else:
    print("No matches found")
