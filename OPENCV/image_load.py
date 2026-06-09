import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is None:
    print("Error Image is not found")
else:
    print("Image loaded succussfully")
 