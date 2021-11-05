import imageio
import imgaug as ia
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from imgaug import augmenters as iaa
import os

dim_size = 736
img_path = os.listdir('Breakthrough Dataset/val_img/')
cnt = 0
output = []
for file in img_path:
    cnt += 1
    label_path = os.listdir('Breakthrough Dataset/val_label/')
    filenames, ext = file.split('.')
    filename = filenames + '.txt'
    bb = []
    bboxes = []
    f = open('Breakthrough Dataset/val_label/'+filename, "r")
    for fline in f:
        line = fline.split(" ")
        '''for l in range(1,5):
            if(float(line[l])<0 or float(line[l])>1):
                print(filenames)'''
        label = int(line[0])
        x_centre = float(line[1])*dim_size
        y_centre = float(line[2])*dim_size
        width = float(line[3])*dim_size
        height = float(line[4])*dim_size
        x1 = x_centre - width/2
        x2 = x_centre + width/2
        y1 = y_centre - height/2
        y2 = y_centre + height/2
        bboxes.append([x1,y1,x2,y2,label])
        output.append([dim_size, dim_size, label, x1,y1,x2,y2,file])
        #print(output)
        #print(bboxes[0][0],bboxes[0][1],bboxes[0][2],bboxes[0][3],bboxes[0][4])


#print(output)

column = ['width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'image_name']
import csv

with open('val.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(column)
    wr.writerows(output)