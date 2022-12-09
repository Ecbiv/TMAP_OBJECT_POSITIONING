from PIL import Image, ImageOps
import numpy as np
import cv2

#only works for 1080x1080 T_Map images



def save_3D_T_Map(outputDir):
    size = 5400

    background = Image.new('RGBA', (size, size), (255, 255, 255, 255))

    #bottom
    img = Image.open('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/bottom.jpg', 'r')
    #img.thumbnail((200,200) )
    img = ImageOps.expand(img,border=5,fill='black')
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (((bg_w - img_w) // 2), ((bg_h - img_h) // 2)-400)
    background.paste(img, offset)

    #trap
    img = Image.open('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/trap.jpg', 'r')
    #img.thumbnail((200,200) )
    img = ImageOps.expand(img,border=5,fill='black')
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (((bg_w - img_w) // 2), ((bg_h - img_h) // 2)+685)
    img = img.transpose(Image.ROTATE_180)
    #img = img.transpose(Image.ROTATE_90)
    background.paste(img, offset)

    #square
    img = Image.open('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/square.jpg', 'r')
    #img.thumbnail((200,200) )
    img = ImageOps.expand(img,border=5,fill='black')
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (((bg_w - img_w) // 2), ((bg_h - img_h) // 2)+1765)
    background.paste(img, offset)

    #circle
    img = Image.open('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/circle.jpg', 'r')
    #img.thumbnail((200,200) )
    img = ImageOps.expand(img,border=5,fill='black')
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (((bg_w - img_w) // 2), ((bg_h - img_h) // 2)-1475)
    background.paste(img, offset)

    #semi
    img = Image.open('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/semi.jpg', 'r')
    #img.thumbnail((200,200) )
    img = ImageOps.expand(img,border=5,fill='black')
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (((bg_w - img_w) // 2)+1085, ((bg_h - img_h) // 2)-400)
    img = img.transpose(Image.ROTATE_90)
    img = img.transpose(Image.ROTATE_90)
    img = img.transpose(Image.ROTATE_90)
    background.paste(img, offset)

    #triangle
    img = Image.open('/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/triangle.jpg', 'r')
    #img.thumbnail((200,200) )
    img = ImageOps.expand(img,border=5,fill='black')
    img_w, img_h = img.size
    bg_w, bg_h = background.size
    offset = (((bg_w - img_w) // 2)-1085, ((bg_h - img_h) // 2)-400)
    img = img.transpose(Image.ROTATE_90)
    background.paste(img, offset)






    background.save(outputDir)
