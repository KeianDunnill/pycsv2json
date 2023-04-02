import csv
import json

data = []

import string

printable = set(string.printable)

def convert_from_file(filePath):
    with open(filePath, "r", newline="", encoding="UTF-8") as f:
        reader = [row for row in csv.reader(f, delimiter=",")]
        header = reader[0]
        
        for row in reader[1:]:
            dictionary = {}
            for headerIndex in range(0,len(header)):
                dictionary[header[headerIndex]] = ''.join(filter(lambda x: x in printable, row[headerIndex])).replace("﻿","")
            data.append(dictionary)

    newFileName = filePath.split("\\")[-1].split(".")[0]
    newFilePath = "\\".join(filePath.split("\\")[:-1])
    with open(newFilePath + "\\" + newFileName + ".json", "w+", encoding="UTF-8") as f:
        f.write(json.dumps(data).replace(', "',', \n        "').replace("\\ufeff","").replace('}, {','\n    }, \n    {\n       ').replace('[{"','[\n    {\n        "').replace('"}]','"\n    }\n]'))

convert_from_file(FILEPATH)

