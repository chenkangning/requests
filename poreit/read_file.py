# -*- coding:utf-8 -*-

import os


def file_move(outDir,outDir2,root_out):
	"""
	查找文件夹内是否存在同文件名的文件
	"""
	for dirs,dirnames,filenames in os.walk(outDir):
		for dir,dirname,filename in os.walk(outDir2):
			for file in filenames:
				lz = os.path.join(dir,file)
				la = os.path.exists(lz)
				if la is True:
					# shutil.move(lz,root_out)
					print(lz)



if __name__ == "__main__":

	outDir = r"H:\CG\kai\drink_\test\v20190505_3"     # 做对比的文件夹
	outDir2 = r"C:\drink\train"                       # 需查看的文件夹
	root_out = r"H:\CG\kai\drink_\test\123"			  # 移出路径
	file_move(outDir,outDir2,root_out)


