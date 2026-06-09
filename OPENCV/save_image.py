import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is not None:
    success=cv2.imwrite("Output_image.png",image)
    if success:
        print("Saved image successfully as Output_image.png")
else:
    print("ERROR")