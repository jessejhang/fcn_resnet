import cv2 as cv


fname = 'Image_2582.png'

img = cv.imread(fname, cv.IMREAD_UNCHANGED)


img = img / 255
print(img)
img = cv.imwrite(fname, img)