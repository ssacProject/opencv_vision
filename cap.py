import cv2
import numpy as np

cap =  cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
heigh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

if cap.isOpened(): # cap 정상동작 확인
  while True:
    ret, frame = cap.read()
    # 프레임이 올바르게 읽히면 ret은 True
    if ret:
        cv2.imshow('ss',frame)
    
    if cv2.waitKey(42) == ord('q'):
        cv2.imwrite('cap_y.jpg',frame)
        break

else:
    print("can't open camera!")
# 작업 완료 후 해제
cap.release()
cv.destroyAllWindows()
