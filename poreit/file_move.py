import shutil
import os
"""
复制子文件夹下的文件
"""
def copy_file(file_one,file_two):
	file_name = os.listdir(file_one)
	for file in file_name:
		file_path = os.path.join(file_one,file)
		file_names = os.listdir(file_path)
		for file in file_names:
			file_paths = os.path.join(file_path,file)
			for file in [os.listdir(file_paths)[1]]:
				file_pathss = os.path.join(file_paths,file)
				# print(file_pathss)
				for dirpath,dirname,filenameq in os.walk(file_pathss):
					for filename in filenameq:
						if os.path.splitext(filename)[1] == ".mp4":
							file_video = os.path.join(dirpath,filename)
							# print(file_video)
							video_file = shutil.copy(file_video,file_two)
							print(video_file)



if __name__ == "__main__":
	file_one = r'H:\CG\kai\platform\video_6_1904'
	file_two = r'H:\CG\kai\platform\123'
	copy_file(file_one,file_two)