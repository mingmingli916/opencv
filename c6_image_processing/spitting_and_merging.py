import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

b, g, r = cv2.split(image)
cv2.imshow('Red', r)
cv2.imshow('Green', g)
cv2.imshow('Blue', b)
cv2.waitKey()

merged = cv2.merge([b, g, r])
cv2.imshow('Merged', merged)
cv2.waitKey()
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow('Red', cv2.merge([zeros, zeros, r]))
cv2.imshow('Green', cv2.merge([zeros, g, zeros]))
cv2.imshow('Blue', cv2.merge([b, zeros, zeros]))

cv2.imwrite('red.jpg', cv2.merge([zeros, zeros, r]))
cv2.imwrite('green.jpg', cv2.merge([zeros, g, zeros]))
cv2.imwrite('blue.jpg', cv2.merge([b, zeros, zeros]))
cv2.waitKey()
