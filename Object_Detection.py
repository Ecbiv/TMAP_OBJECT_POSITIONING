import subprocess
from pathlib import Path
import re

def format_output(outputDir):
    objects = []
    file = open(outputDir)
    lines = file.readlines()

    atObjects = False
    for line in lines:
        if '%' in line:
            atObjects = True
        
        if atObjects:
            name = line[0:line.find(':')]
            #acc = line[line.rfind('%')-2:line.rfind('%')]
            numbers = re.findall(r'[+-]?\d+', line)
            numBad = sum(1 for number in numbers if int(number) < 0)
            if numBad == 0 and int(numbers[3]) < 400 and int(numbers[4]) < 400:
                objects.append([name,numbers[0],numbers[1],numbers[2],numbers[3],numbers[4]])
        for object in objects:
            repeats = sum(1 for name in objects if object[0] in name)
            if repeats > 1:
                objects = list(filter(lambda obj: object[0] not in obj, objects))
    return objects

def detect(imageDir, outputDir):
    #subprocess.run('bash', shell=True, check=True,)
    print(subprocess.run(f"./darknet detect cfg/yolov4.cfg yolov4.weights -ext_output {imageDir} > {outputDir}", shell=True, check=True, cwd="/mnt/c/Users/Tomca/Documents/darknet"))

    return format_output(outputDir)
    



#objects = detect('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/download_1080x1080.jpg','/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/output.json')

#print(objects)