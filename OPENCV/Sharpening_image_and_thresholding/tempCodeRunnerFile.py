import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\xc.jpg",cv2.IMREAD_GRAYSCALE)
 
if image is not None:
    thresh=cv2.threshold(image,120,255,cv2.THRESH_BINARY)
    cv2.imshow("Real image",image)
    cv2.imshow("Thresholded image",thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not found")