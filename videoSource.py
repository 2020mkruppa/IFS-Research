import cv2

def getWidth():
	return 896

def getHeight():
	return 448

def getSpectraPartition():
	return 696

# -------------------------Width
# |                  |
# |                  |
# |     spectra      |  real
# |      lines       |  image
# |                  |
# H                 Part.
class VideoSource:
	def __init__(self, filename, skip=0):
		self.video = cv2.VideoCapture(filename)
		for i in range(skip):
			ret, frame = self.video.read()
		self.frameNum = 0

	def getFrame(self):
		self.frameNum += 1
		ret, f = self.video.read()
		if not ret or self.frameNum == 2100:
			return None, self.frameNum
		return f, self.frameNum

	def destroy(self):
		self.video.release()