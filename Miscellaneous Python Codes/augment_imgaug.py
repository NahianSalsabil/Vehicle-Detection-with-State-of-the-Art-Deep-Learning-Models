import imageio
import imgaug as ia
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
from imgaug import augmenters as iaa
import os

dim_size = 736
img_path = os.listdir('test/img/')

for file in img_path:
    output = []
    image = imageio.imread('test/img/'+file)
    image = ia.imresize_single_image(image, (dim_size, dim_size))

    label_path = os.listdir('test/label/')
    filenames, ext = file.split('.')
    filename = filenames + '.txt'
    bb = []
    bboxes = []
    f = open('test/label/'+filename, "r")
    for fline in f:
        line = fline.split(" ")
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
        #print(bboxes)
        #print(bboxes[0][0],bboxes[0][1],bboxes[0][2],bboxes[0][3],bboxes[0][4])

    for boxes in bboxes:
        bb.append(BoundingBox(boxes[0], boxes[1], boxes[2], boxes[3], boxes[4]))


    bbs = BoundingBoxesOnImage([
    bb[x] for x in range(len(bb))
    ], shape=(dim_size, dim_size))

    #ia.imshow(bbs.draw_on_image(image, size=2))

    seq = iaa.Noop()

    '''iaa.OneOf([
        iaa.Sequential([
            iaa.pillike.Equalize(),
            iaa.TranslateY(percent=(-0.4, 0.4))
        ]),
        iaa.Sequential([
            iaa.Rotate((-20, 20)),
            iaa.Rotate((-30, 30))
        ]),
        iaa.Sequential([
            iaa.pillike.EnhanceSharpness(),
            iaa.TranslateY(percent=(-0.4, 0.4))
        ]),
        iaa.Sequential([
            iaa.Rotate((-45, 45)),
            iaa.pillike.Autocontrast((10, 20), per_channel=True)
        ]),
        iaa.Sequential([
            iaa.pillike.Equalize(),
            iaa.Solarize(0.5, threshold=(32, 128))
        ]),
        iaa.Sequential([
            iaa.pillike.EnhanceColor(),
            iaa.TranslateX(percent=(-0.4, 0.4))
        ]),
        iaa.Rotate((-45, 45)),
        iaa.TranslateY(percent=(-0.4, 0.4)),
    ])'''

    image_aug, bbs_aug = seq(image=image, bounding_boxes=bbs)
    #ia.imshow(bbs_aug.draw_on_image(image_aug, size=2))
    try:
        imageio.imwrite('test/conv_img/' + filenames + '_aug1.' + ext, image_aug[:, :, :])
    except:
        print(filenames + "e jhamela")
        continue



    for i in enumerate(bbs_aug):
        box = bbs_aug[i[0]]
        label = bboxes[i[0]][4]

        x1 = max(min(box[0][0],dim_size),0)
        y1 = max(min(box[0][1],dim_size),0)
        x2 = max(min(box[1][0],dim_size),0)
        y2 = max(min(box[1][1],dim_size),0)
        #print(box)
        #print(x1, y1, x2, y2, label)

        x_centre = (x1+x2)/(2*dim_size)
        y_centre = (y1+y2)/(2*dim_size)
        width = (x2-x1)/(dim_size)
        height = (y2-y1)/(dim_size)
        #print(label, x_centre, y_centre, width, height)
        output.append([label, x_centre, y_centre, width, height])

    with open('test/conv_label/'+ filenames + '_aug1.txt', "w") as out:
        for line in output:
            for val in line:
                out.write(str(val)+" ")
            out.write("\n")
    #print(filenames)


'''
seq = iaa.OneOf([
                    iaa.Sequential([
                        iaa.pillike.Equalize(),
                        iaa.TranslateY(percent=(-0.3, 0.3))
                    ]),
                    iaa.Sequential([
                        iaa.Rotate((-20, 20)),
                        iaa.Rotate((-30, 30))
                    ]),
                    iaa.Sequential([
                        iaa.pillike.EnhanceSharpness(),
                        iaa.TranslateY(percent=(-0.3, 0.3))
                    ]),
                    iaa.Sequential([
                        iaa.Rotate((-45, 45)),
                        iaa.pillike.Autocontrast((10, 20), per_channel=True)
                    ]),
                    iaa.Sequential([
                        iaa.pillike.Equalize(),
                        iaa.Solarize(0.5, threshold=(32, 128))
                    ]),
                    iaa.Sequential([
                        iaa.pillike.EnhanceColor(),
                        iaa.TranslateX(percent=(-0.3, 0.3))
                    ]),
                    iaa.Rotate((-45, 45)),
                    iaa.TranslateY(percent=(-0.4, 0.4)),
         ])
'''

'''seq = iaa.OneOf([
                    iaa.Rotate((-50, -30)),
                    iaa.Rotate((30, 50)),
                    iaa.TranslateY(percent=(-0.4, -0.2)),
                    iaa.TranslateY(percent=(0.2, 0.4)),
                    iaa.Sequential([
                        iaa.pillike.Equalize(),
                        iaa.TranslateX(percent=(-0.4, -0.2)),
                    ]),
                    iaa.Sequential([
                        iaa.pillike.Equalize(),
                        iaa.TranslateX(percent=(0.2, 0.4)),
                    ]),
         ])'''