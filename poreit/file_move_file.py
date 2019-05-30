import os
import shutil
from glob import glob

class File():
	def __init__(self,outDir,outDir2,imageDir):
		self.outDir = outDir
		self.outDir2 = outDir2
		self.imageDir = imageDir
		self.imgname1 = []
		self.imgname2 = []


	def file_move(self):
		image1 = []

		self.imageList = glob(os.path.join(self.outDir,"*.png"))
		for item in self.imageList:
			image1.append(os.path.basename(item))
		for item in image1:
			(temp1,temp2) = (os.path.splitext(item))
			self.imgname1.append(temp1)

	def file_moves(self):
		image2 = []

		imageList2 = glob(os.path.join(self.outDir2,"*.png"))
		for item in imageList2:
			image2.append(os.path.basename(item))
		for item in image2:
			(temp1,temp2) = os.path.splitext(item)
			self.imgname2.append(temp1)

	def file_sh(self):
		for item1 in self.imgname1:
			for item2 in self.imgname2:
				if item1 == item2:
					dir = self.imageList[self.imgname1.index(item1)]
					img = shutil.move(dir,imageDir)
					print(img)

if __name__=="__main__":
	outDir = r"H:\CG\kai\drink_\test\v20190505\test\neg_use\neg_cut\smoke" # 移动路径
	outDir2 = r"H:\CG\kai\drink_\test\v20190505_2\v20190505\neg_use\smoke"  # 比较路径
	imageDir = r"H:\CG\kai\drink_\test\v20190505_3\neg_use\smoke" # 移至路径
	file = File(outDir,outDir2,imageDir)
	file.file_move()
	file.file_moves()
	file.file_sh()

