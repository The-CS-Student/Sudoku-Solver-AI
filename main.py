import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image
import solve

Digits = "123456789"
board = []
def predict(image):
	
	image = Image.fromarray(image)
	text = pytesseract.image_to_string(image, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
	if text not in Digits:
		return 0
	
	return text
	

def getBoard(filename):
	image = cv2.imread(filename,0)
	image = cv2.GaussianBlur(image,(9,9),10)
	

	# kernel = np.ones((3,3), np.uint8) 
	# th3 = cv2.dilate(th3,kernel,iterations=1)
	


	# plt.imshow(images[0],'gray')
	height = np.size(image,0)
	width = np.size(image,1)
	cellH = round(height/9)
	cellW = round(width/9)
	cellBoard = []

	for i in range(9):
		arr = []

		for j in range(9):
			
			crop_img = image[i*cellH:cellH*(i+1), j*cellW:cellW*(j+1)]
			
			
			arr.append(predict(crop_img))
			
			
		cellBoard.append(arr)
	return cellBoard
def main(filename):
	board = getBoard(filename)
	
	for i in range(9):
		for j in range(9):
			if(board[i][j]==''):
				board[i][j] = 0
			

	for i in range(9):
		for j in range(9):
			print(board[i][j],end=" ")
			print(" ",end="")
		print(" ")
	print(" ")
	solve.solveSudoku(board)
	for i in range(9):
		for j in range(9):
			print(board[i][j],end=" ")
			print(" ",end="")
		print(" ")
def run():
	if(len(sys.argv)==0):
		print("Add Filepath")
		print(" ")
		sys.quit()
	filename = sys.argv[1]
	main(filename)
run()
