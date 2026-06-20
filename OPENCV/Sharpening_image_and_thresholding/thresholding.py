import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\camraman.webp",cv2.IMREAD_GRAYSCALE)
 
if image is not None:
    ret,thresh=cv2.threshold(image,0,255,cv2.THRESH_BINARY)#if thresh=0 OpenCV analyzed the image and decided that 137 is the best threshold.
    cv2.imshow("Real image",image)
    cv2.imshow("Thresholded image",thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not found")

# thresh>value->0 
# thresh<value->255 white
