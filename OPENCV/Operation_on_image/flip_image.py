import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is not None:
    cv2.imshow("Real image",image)
    flip_vertical=cv2.flip(image,0)
    cv2.imshow("Flipped image",flip_vertical)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not found")