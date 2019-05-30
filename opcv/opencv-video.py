import cv2
import time

interval = 60             # 捕获图像的间隔，单位：秒
num_frames = 500          # 捕获图像的总帧数
out_fps = 24              # 输出文件的帧数

#VideoCapyure用于获取相机设备并捕获图像和视频，或是从文件中捕获
#VideoCapture(0)表示打开默认的相机
cap = cv2.VideoCapture(0)

#获取捕获的分辨率
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#VideoWriter用于生成视频
#设置要保存视频的编码，分辨率和帧率
video = cv2.VideoWriter(
	"time_lapse.avi",
	cv2.VideoWriter_fourcc('M','P','4','2'),
	out_fps,
	size
)

#对于一些低画质的摄像头，前面的帧可能不稳定，略过
for i in range(42):
	cap.read()

# 开始捕获，通过read()函数获取捕获的帧

try:
	for i in range(num_frames):
		_, frame = cap.read()
		video.write(frame)

except KeyboardInterrupt:
	# 提前停止捕获
	print('topped!{}/{} frames captured!'.format(i, num_frames))

	# 释放资源并写入视频文件
	video.release()
	cap.release()