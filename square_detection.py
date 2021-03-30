import cv2
import numpy as np

img =cv2.imread('photo_g1.jpg')   
cv2.imshow('img',img)                                          # 원본이미지 ,        " 비교확인용"
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                  # 이미지스케일 변환       

ret,imthres = cv2.threshold(imgray,180,255,cv2.THRESH_BINARY)  # 바이너리로 파일로 변환 
cv2.imshow('threshold',imthres)                                # threshould " 비교확인용"

# 컨투어를 
contour, hierachy = cv2.findContours(imthres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#x,y,w,h = cv2.boundingRect(contour[2])                          # cv2.boundingRect 함수를 통해 countour[2] 값의 좌표값 추출
#print(len(contour))                                             

#cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)                   #  추출된 좌표값을 통해 사각형 그림 


#rect = cv2.minAreaRect(contour[2])
#box = cv2.boxPoints(rect)
#box = np.int0(box)
#cv2.drawContours(img,[box],-1,(0,255,0),3)



cv2.drawContours(img,contour,-1,(0,255,0),4)                     # 컨투어 라인을 출력 한다.

# 화면 출력시 
img[0:,150]=150                                         
img[150,]=150
cv2.imshow('result_img',img)




cv2.waitKey(0)
cv2.destroyAllWindows()
