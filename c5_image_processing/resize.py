import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

r = 150.0 / image.shape[1]  # width
dim = 150, int(image.shape[0] * r)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized (Width)', resized)

r = 50.0 / image.shape[0]  # height
dim = int(image.shape[1] * r), 50
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized (Height)', resized)

resized = imutils.resize(image, width=100)
cv2.imshow('Resized via Function', resized)

cv2.waitKey()
