#coding=utf-8


import itchat
from PIL import Image
import os
import math


#下载好友头像
def download_images(frined_list):
    image_dir = "./images/"
    num = 1
    for friend in frined_list:
        image_name = str(num)+'.jpg'
        num+=1
        img = itchat.get_head_img(userName=friend["UserName"])
        with open(image_dir+image_name, 'wb') as file:
            file.write(img)

def merge_images(path):
    print("Merging head images......")
    photo_width = 200
    photo_height = 200

    photo_list = []
    dirName = os.getcwd()+path
    print(dirName)

    for root, dirs, files in os.walk(dirName):
        for file in files:
            if "jpg" in file and os.path.getsize(os.path.join(root, file)) > 0:
                photo_list.append(os.path.join(root, file))

    pic_num = len(photo_list)
    line_max = int(math.sqrt(pic_num))
    row_max = int(math.sqrt(pic_num))
    print(line_max, row_max, pic_num)

    if line_max > 20:
        line_max = 20
        row_max = 20
    
    num = 0
    pic_max=line_max*row_max

    toImage = Image.new('RGBA',(photo_width*line_max, photo_height*row_max))

    for i in range(0,row_max):
        for j in range(0,line_max):
            pic_fole_head = Image.open(photo_list[num])
            tmppic = pic_fole_head.resize((photo_width,photo_height))

            loc = (int(j%row_max*photo_width),int(i%row_max*photo_height))
            toImage.paste(tmppic,loc)
            num = num+1
            if num >= len(photo_list):
                break
        if num >= pic_max:
            break
    print(toImage.size)
    toImage.save('merged.png')


if __name__ == '__main__':
    
    #itchat.auto_login()
    #friends = itchat.get_friends(update=True)#获取好友信息
    #download_images(friends)
    
    merge_images('/images/')