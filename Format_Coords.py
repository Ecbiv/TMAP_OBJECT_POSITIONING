import Object_Detection as od
import csv




def detect_and_filter_loners(obj1Dir,obj1ODir,obj2Dir,obj2ODir):
    objects1 = od.detect(obj1Dir,obj1ODir)
    objects2 = od.detect(obj2Dir,obj2ODir)

    for object in objects1:
                repeats = sum(1 for object2 in objects2 if object[0] in object2)
                if repeats < 1:
                    objects1 = list(filter(lambda obj: object[0] in obj, objects1))
                    objects2 = list(filter(lambda obj: object[0] in obj, objects2))

    
    return objects1,objects2


def save_csv(outputDir,obj1ODir,obj2ODir):

    obj1Dir = ''
    obj2Dir = ''    
    side1 = ''
    side2 = ''
    sides = open('sides.csv')
    csv_in = csv.reader(sides, delimiter=',')
    count = 0
    for line in csv_in:
        if count == 0:
            obj1Dir = line[0]
            side1 = line[1]
        else:
            obj2Dir = line[0]
            side2 = line[1]
        count+=1

    print(f'1:{obj1Dir}, 2:{obj2Dir}')
    objects1,objects2 = detect_and_filter_loners(obj1Dir,obj1ODir,obj2Dir,obj2ODir)

    objects1.sort(key=lambda object: object[0])
    objects2.sort(key=lambda object: object[0])

    
    file = open(outputDir, 'w')
    writer = csv.writer(file)
    for i in range(len(objects1)):
        writer.writerow((objects1[i][0],side1,objects1[i][1],objects1[i][2],objects1[i][3],objects1[i][4],objects1[i][5]))
        writer.writerow((objects2[i][0],side2,objects2[i][1],objects2[i][2],objects2[i][3],objects2[i][4],objects2[i][5]))

    file.close()

