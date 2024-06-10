import os

json = open("songs.json", "w", encoding="utf-8")
json.write('{\n    "songs":[\n')
i = 0

for file in os.listdir():
    i += 1
    if file[-4:] != ".ogg":
        continue
    json.write("        {\n" + '            "name":' + '"' + file.replace(".ogg","") + '",' + "\n")
    json.write('            "url":' + '"' + 'https://github.com/patrlim/musicshite/raw/main/' + file.replace(" ","%20") + '"' + "\n        }")
    if i != len(os.listdir()):
        json.write(",")
    json.write("\n")
json.write('    ]\n}')