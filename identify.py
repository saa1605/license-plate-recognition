import numpy as np
import cv2
import sys

import pytesseract
 
if __name__ == '__main__':
      
  # Uncomment the line below to provide path to tesseract manually
  # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
  config = ('-l eng --oem 1 --psm 3')
  


  # Read image from disk
  im = cv2.imread('car.jpg')
  x,y,w,h = cv2.selectROI(im)
  print x,y,w,h
  bbox = im[300:370,300:600]

  gray = cv2.cvtColor(bbox, cv2.COLOR_BGR2GRAY)
  cv2.imshow('im',gray)
  cv2.waitKey(0)
  # Run tesseract OCR on image
  text = pytesseract.image_to_string(gray, config=config)
 
  # Print recognized text
  print(text)