import cv2
import numpy as np
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\camel.jpg")
kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
if image is not None:
    sharpened_image=cv2.filter2D(image,-1,kernel)
    cv2.imshow("Real image",image)
    cv2.imshow("Sharpened image",sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not found")