'''
    @File: main.c
    @Author: Jabed Akhtar
    @Info: Threshold for Images Colors will not work perfect for all Pictures, you can check/change it
'''

# standard needed libraries
import cv2 as cv
import numpy as np

# loading image from Directory
# !!! Here you can set path to your Image
# I have here three Pictures for checking
img_path = r'Path\to\Images\Image_Color_Detection_n_Segmentation__Red_White_Yellow\Pictures\Butterfly.jpg'

# reading Image ----------------------------------------
img = cv.imread(img_path)
img = cv.resize(img,  (960, 540))
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# showing the image
cv.imshow("Original Image", img)
cv.waitKey(0) # press any key to close the window

# Detecting Yellow Colour ------------------------------
lower_yel = np.array([20,100,100], dtype=np.uint8)
upper_yel = np.array([60,150,255], dtype=np.uint8)
yel_mask = cv.inRange(img_hsv, lower_yel, upper_yel) # masking image with lower and upper threshold
yel_img = cv.bitwise_and(img_hsv, img_hsv, mask=yel_mask) # getting yellow image
cv.imshow("Yellow_Image", yel_img) # showing Image
cv.waitKey(0)

# Detecting Red Colour ---------------------------------
lower_red1 = [0,50,50]
higher_red1 = [10,255,255]
lower_red2 = [0,185,185]
higher_red2 = [1,255,255]
lower_red3 = [170,50,50]
higher_red3 = [180,255,255]
low_red = np.array(lower_red3)
high_red = np.array(higher_red3)
red_mask = cv.inRange(img_hsv, low_red, high_red)  # masking image with lower and upper threshold
red_img = cv.bitwise_and(img_hsv, img_hsv, mask=red_mask)  # getting yellow image
cv.imshow("Red_Image", red_img)
cv.waitKey(0)

# Detecting White Colour ---------------------------------
lower_white1 = np.array([0,0,0], dtype=np.uint8)
upper_white1 = np.array([0,0,255], dtype=np.uint8)
lower_white2 = np.array([0,0,242], dtype=np.uint8)
upper_white1 = np.array([0,0,255], dtype=np.uint8)
lower_white3 = np.array([0,0,0], dtype=np.uint8)
upper_white3 = np.array([0,0,255], dtype=np.uint8)
low_whi = np.array(lower_white3)
high_whi = np.array(upper_white3)
white_mask = cv.inRange(img_hsv, low_whi, high_whi)  # masking image with lower and upper threshold
white_img = cv.bitwise_and(img_hsv, img_hsv, mask=white_mask)  # getting yellow image
cv.imshow("White_Image", white_img)
cv.waitKey(0)

# Combining Images -------------------------------------
# Yellow and Red
ye_re_img = cv.bitwise_or(yel_img, red_img)
#img_yr = cv.addWeighted(yel_img, 1, red_img, 1, 0)
cv.imshow("Yellow-Red-Image", ye_re_img)
cv.waitKey(0)

# Yellow, Red and White
ye_re_wh_img = cv.bitwise_or(ye_re_img, white_img)
#img_yrw = cv.addWeighted(ye_re_img, 1, white_img, 1, 0)
cv.imshow("Yellow-Red-White-Image", ye_re_wh_img)
cv.waitKey(0)

# -------------- END OF FILE ---------------------
