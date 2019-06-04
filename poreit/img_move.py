#！/usr/bin/python
# -*- coding:utf-8 -*-

import os
import shutil
def file_name(file_dir,file_mv):
	for dirpath,drinames,filenames in os.walk(file_dir):
		for file in filenames:
			if os.path.splitext(file)[1] == ".png":
				file_images = os.path.join(dirpath,file)
				images_move = shutil.move(file_images,file_mv)
				print(images_move)



if __name__== "__main__":
	file_dir = r"H:\CG\kai\drink_\test\v20190505\test\neg_use\neg_cut"
	file_mv = r"H:\CG\kai\drink_\test\v20190505\test\neg_use"
	file_name(file_dir,file_mv)
