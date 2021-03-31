import cv2
import numpy as np

area_max = 20000
area_min = 4000
min_with =  40      
min_heigh = 40

#min_ratio, max_ratio = 0.7, 1.3

cap =  cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
heigh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width ,heigh )


def prepocessing(frame):
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    ret,imthres = cv2.threshold(imgray,155,255,cv2.THRESH_BINARY)      # preproccessing
                         
    contours,hierarchy = cv2.findContours(imthres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)  
        area = w*h
        #ratio = h/w

        if  area_max > area > area_min and 100> w > min_with and 100> h > min_heigh :  ## and min_ratio > ratio > max_ratio
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
           # print(x,y,w,h)
    cv2.imshow('Otter', frame)

if cap.isOpened(): # cap 정상동작 확인
  while True:
    ret, frame = cap.read()
    # 프레임이 올바르게 읽히면 ret은 True
    if ret is True:
     
        prepocessing(frame)
     
    else:
        print("can't read frame , err!!!")
        break
    
    if cv2.waitKey(42) == ord('q'):
       
        break
else:
    print("can't open camera!")
# 작업 완료 후 해제
cap.release()
cv.destroyAllWindows()
