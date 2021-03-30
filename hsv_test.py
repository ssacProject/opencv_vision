import cv2
import numpy as np

img =cv2.imread('photo_g1.jpg')              # 이미지 읽기

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)    # 이미지 스케일변환

h,s,v = cv2.split(hsv)     # 색공간  H,S,V 으로 분할 

h = cv2.inRange(h,30,35)   # h값을 30~35 범위 값으로 추출

square = cv2.bitwise_and(hsv,hsv,mask=h)          # hsv 이미지와 마스킹 값을 and 연산 수행하여 마스킹 값만 필터링    
square = cv2.cvtColor(square, cv2.COLOR_HSV2BGR)  # 필터링된 이미지를  hsv > bgr 이미지로 변환


cv2.imshow('square',square)   # h값을 추출한 이미지
cv2.imshow('img',img)         # 원본이미지
cv2.imshow('h',h)             
cv2.imshow('s',s)
cv2.imshow('v',v)
cv2.waitKey(0)
cv2.destroyAllWindows()

