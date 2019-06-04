import numpy as np
import cv2

#定义宽600，高400的画布，初始化为白色
canvas = np.zeros((400,600,3),dtype=np.uint8)+255

#画一条纵向的正中只的黑色分界线
cv2.line(canvas,(300,399),(300,0),(0,0,0),2)

#画一条右半部份画面以150为界的横向分界线
cv2.line(canvas,(300,149),(599,149),(0,0,0),2)


#左半部分的右下角画个蓝色的矩形
cv2.circle(canvas,(450,260),75,(255,0,255),5)

#定义两个三角形，并执行内部绿色填充
tiangles = np.array([
	[(200,240),(145,333),(255,333)],
	[(60,180),(20,237),(100,237)],
])
cv2.fillPoly(canvas,tiangles,(0,255,0))

#在左半部分最上方打印文字
cv2.putText(canvas,'Python-opencv',(5,15),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),1)
