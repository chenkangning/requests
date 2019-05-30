# -*- coding=utf-8 -*-

import os
from glob import glob
import numpy as np
import cv2
import shutil

def main(root,dira,file):
    file_img = glob(os.path.join(root,"*.png"))
    f_dict = {}
    for f_name in file_img:
        name = os.path.splitext(os.path.basename(f_name))[0]
        lines = name.split('_')[-4:]
        bboxes = np.array(lines).astype(np.int)
        f_name = os.path.join(dira, name.replace("_{}_{}_{}_{}_{}".format(name.split('_')[-5], bboxes[0],bboxes[1],bboxes[2], bboxes[3]), ".png"))
        if f_name in f_dict:
            f_dict[f_name].append(bboxes)
        else:
            f_dict[f_name] = [bboxes]

    for key in f_dict:
        bboxes = f_dict[key]
        f_txt = key.replace('.png','.txt')

        f_txt = f_txt.replace(dira, file)


        f = open(f_txt,'w')

        strw =  "{}\n".format(len(bboxes))
        for bbox in bboxes:
            strw += "car {} {} {} {} 0 0 0 0\n".format(bbox[0], bbox[1], bbox[2], bbox[3])
        f.write(strw)
        f.close()

        print(key, bboxes)
        img = cv2.imread(key)
        if img is None:
            continue

        x1 = bboxes[0][0]
        y1 = bboxes[0][1]
        x2 = x1 + bboxes[0][2]
        y2 = y1 + bboxes[0][3]

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.imshow("im", img)
        cv2.waitKey(1)
        shutil.move(key, file)




if __name__ == "__main__":
    root = 'H:/CG/tsd/datasets/complete/20190327/img_r'
    dira = 'H:/CG/tsd/datasets/complete/20190327/org/'
    file = 'H:/CG/tsd/datasets/complete/20190327/1/'
    main(root,dira,file)