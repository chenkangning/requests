import cv2
import  os
import shutil

img = r"H:\CG\tsd\aaa\sample\point_img"
imgs = r"H:\CG\tsd\aaa\sample\image"
for i in os.listdir(img):
    images = os.path.join(img,i)
    imag = cv2.imread(images)
    # print(imag.size[1])
    if imag.shape[1] <= 40:
        move = shutil.move(images,imgs)
        print(move)