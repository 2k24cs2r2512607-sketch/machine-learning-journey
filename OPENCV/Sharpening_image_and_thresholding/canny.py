import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\man.webp",cv2.IMREAD_GRAYSCALE)
 
if image is not None:
   
    blur = cv2.GaussianBlur(image, (5,5), 0)
    edges = cv2.Canny(blur, 100, 200)
    cv2.imshow("Real image",image)
    cv2.imshow("Blurred image",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not found")