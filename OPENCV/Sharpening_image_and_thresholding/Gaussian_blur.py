import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\wall.jpg")
 
if image is not None:
    blur=cv2.GaussianBlur(image,(11,11),3)
    cv2.imshow("Real image",image)
    cv2.imshow("Blurred image",blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not found")