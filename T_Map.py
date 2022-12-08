import profiles
import numpy as np
import cv2


def make_t_map(coordsDir = 'coords.csv', size = 1080):


    profileList = profiles.directionalOrientationalAllignment(coordsDir, size)


    circle = np.full((size,size), 255).astype(np.uint8)
    triangle = np.full((size,size), 255).astype(np.uint8)
    trap = np.full((size,size), 255).astype(np.uint8)
    semi = np.full((size,size), 255).astype(np.uint8)
    square = np.full((size,size), 255).astype(np.uint8)
    bottom = np.full((size,size), 255).astype(np.uint8)

    for profile in profileList:
        print(profile)
        #circle
        start = (int(profile[1]),int(profile[2]))
        startText = (int(profile[1]),int(profile[2])-10)
        end = (int(profile[1]+profile[5]),int(profile[2]+profile[4]))
        circle = cv2.rectangle(circle, start, end, 0, 4)
        circle = cv2.putText(circle, profile[0], startText, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        cv2.imwrite('circle.jpg', circle)

        #triangle
        start = (size -int(profile[3]-profile[6]),int(profile[2]))
        startText = (size - int(profile[3]-profile[6]),int(profile[2])-10)
        end = (size - int(profile[3]),int(profile[2]+profile[4]))
        triangle = cv2.rectangle(triangle, start, end, 0, 4)
        triangle = cv2.putText(triangle, profile[0], startText, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        cv2.imwrite('triangle.jpg', triangle)

        #trap
        start = (size - int(profile[1]),int(profile[2]))
        startText = (size - int(profile[1]),int(profile[2])-10)
        end = (size-int(profile[1]+profile[5]),int(profile[2]+profile[4]))
        trap = cv2.rectangle(trap, start, end, 0, 4)
        trap= cv2.putText(trap, profile[0], startText, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        cv2.imwrite('trap.jpg', trap)

        #semi
        start = (int(profile[3]),int(profile[2]))
        startText = (int(profile[3]-int(profile[6])),int(profile[2])-10)
        end = (int(profile[3]+profile[6]),int(profile[2]+profile[4]))
        semi = cv2.rectangle(semi, start, end, 0, 4)
        semi = cv2.putText(semi, profile[0], startText, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        cv2.imwrite('semi.jpg', semi)

        #square
        #TODO
        start = (int(profile[1]),size - int(profile[3]))
        startText = (int(profile[1]), size - int(profile[3])-10)
        end = (int(profile[1]+profile[5]), size - int(profile[3]+profile[6]))
        square = cv2.rectangle(square, start, end, 0, 4)
        square = cv2.putText(square, profile[0], startText, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        cv2.imwrite('square.jpg', square)

        #bottom
        start = (int(profile[1]),int(profile[3]))
        startText = (int(profile[1]),int(profile[3])-10)
        end = (int(profile[1]+profile[5]),int(profile[3]+profile[6]))
        bottom = cv2.rectangle(bottom, start, end, 0, 4)
        bottom = cv2.putText(bottom, profile[0], startText, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
        cv2.imwrite('bottom.jpg', bottom)

    #cv2.imshow('test',trap)
    #cv2.waitKey()







