import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is not None:
    crop=image[100:200,50:100]
    cv2.imshow("Real image",image)
    cv2.imshow("Cropped image",crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image is not found")