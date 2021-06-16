filename = "file.txt"

with open(filename) as file:
    content = file.readlines()
    content = [x.strip() for x in content]

for i in range(0, len(content)):
    if i % 2 != 0:
        print(content[i])

