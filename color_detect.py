#2021-04-01    
import cv2
import numpy as np
import time 
area_max = 20000
area_min = 10000
min_with =  40      
min_heigh = 40
fps = 10
delay = int(1000/fps)

#color_filter
lower_yellow = (20,30,30)
upper_yellow = (35,255,255)

lower_green = (45,50,50)
upper_green = (90,255,255)


def filter(frame_img):
    # convert image to  hsv_image 
    hsv = cv2.cvtColor(frame_img,cv2.COLOR_BGR2HSV)
    #make filter each
    mask_yellow = cv2.inRange(hsv,lower_yellow,upper_yellow)
    mask_green  = cv2.inRange(hsv,lower_green,upper_green)

    img_result_yellow = cv2.bitwise_and(frame_img,frame_img, mask= mask_yellow)
    img_result_g = cv2.bitwise_and(frame_img,frame_img, mask= mask_green)
    
    if np.sum(img_result_yellow) > np.sum(img_result_g) :
        # judge yellow
        img_result = img_result_yellow
        Text_color = 'yellow'
        # print('yellow sum :' +str(np.sum(img_result_yellow)))
        # cv2.imshow('yellow', img_result)
        #print('yellow :'+str(np.sum(img_result_yellow)))
    elif np.sum(img_result_g) > np.sum(img_result_yellow) :
        # judge yellow    
        k= cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        opening = cv2.morphologyEx(img_result_g, cv2.MORPH_OPEN, k)
        img_result = opening
        Text_color = 'green'
        # cv2.imshow('green', img_result)
        # print('green sum :' +str(np.sum(img_result_g)))
        #print('green :'+str(np.sum(img_result_g)))
    else:
        return 0
    return img_result ,Text_color
#min_ratio, max_ratio = 0.7, 1.3

cap =  cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
heigh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(width ,heigh )

# width/2 , heigh/2

def prepocessing(frame):
    
    img_result , Text_color = filter(frame)

    gray = cv2.cvtColor(img_result,cv2.COLOR_BGR2GRAY)

    ret_g,imthres = cv2.threshold(gray,70,255,cv2.THRESH_BINARY) 
    cv2.imshow('gray',imthres)
    contours,hierarchy = cv2.findContours(imthres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)  
        area = w*h
        #ratio = h/w
        
        print(len(contours))
        if  area > area_min  and 120> w > min_with and 120 > h > min_heigh :  ## and min_ratio > ratio > max_ratio
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            #print(x,y,h,w)
            xpos=int((x+w)/2)
            ypos=int((y+h+100))
            cv2.putText(frame,Text_color,(xpos,ypos),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
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
    
    if cv2.waitKey(delay) == ord('q'):
       
        break
else:
    print("can't open camera!")
# 작업 완료 후 해제
cap.release()
cv2.destroyAllWindows()




