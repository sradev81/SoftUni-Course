

text = input()
capitals = []

for index, letter in enumerate(text):
    if letter.isupper():
        capitals.append(index)

print(capitals)
