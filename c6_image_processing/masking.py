import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(mask, (185, 30), (240, 84), 255, -1)
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mask Applied to Image', masked)

cv2.waitKey()
