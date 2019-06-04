import cv2
import numpy as np
from matplotlib import pyplot as plt
img0 = cv2.imread('D:/vscode/vscode_img/timg.jpg')
# 读取图片

img_200x200 = cv2.resize(img,(200,200))
#缩放图片

img_200x300 = cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
# print(cv2.imwrite("a.jpg",img_200x300))
#不直接指定缩放大小，通过fx和fy指定缩放比例，0.5则长宽都为原来的一半
#插值方法默认cv2.INTEP_LINEAR,这里指定为最近邻插值

img_300x300 = cv2.copyMakeBorder(img,50,50,0,0,cv2.BORDER_CONSTANT,value=(250,0,0))
# print(cv2.imwrite("aa.jpg",img_300x300))
#上下各贴50像素的黑边。

path_tree = img[20:150,-180:-60]
# cv2.imwrite('2.jpg',path_tree)
#剪裁

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)               #通过cv2.cvtColoru把图像从BGR转换到HSV
turn_green_hsv = img_hsv.copy()
turn_green_hsv[:,:,0] = (turn_green_hsv[:,:,0] + 15)%180
turn_green_img = cv2.cvtColor(turn_green_hsv,cv2.COLOR_HSV2BGR)
# cv2.imwrite('turn.jpg',turn_green_img)

colorless_hsv = img_hsv.copy()
colorless_hsv[:,:,1] = 0.5*colorless_hsv[:,:,1]
colorless_img = cv2.cvtColor(colorless_hsv,cv2.COLOR_HSV2BGR)
# cv2.imwrite("a.jpg",colorless_img)


darker_hsv = img_hsv.copy()
darker_hsv[:,:,2] = 0.5*darker_hsv[:,:,2]
darker_img = cv2.cvtColor(darker_hsv,cv2.COLOR_HSV2BGR)
# cv2.imwrite("aas.jpg",darker_img)

