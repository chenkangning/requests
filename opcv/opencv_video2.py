import cv2
import os
import sys

#第一个输入参数是包含视频片段的路径
input_path = sys.argv[1]

#第二个输入参数是设定每隔多少帧截取一帧
frame_interval = int(sys.argv[2])

#列出文件夹下所有的视频文件
filenames = os.listdir(input_path)

#获取文件夹名称
video_prefix = input_path.spilt(os.sep)[-1]

#建立一个新的文件夹，名称为原文件夹名称后加上_frames
frame_path = '{}_frames'.format(input_path)
if not os.path.exists(frame_path):
	os.mkdir(frame_path)

#初始化一个VideoCapture对象
cap = cv2.VideoCapture()

#遍历所有文件
for filename in filenames:
	filename = os.sep.join([input_path,filename])

#执行结束释放资源
cap.release()