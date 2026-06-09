import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is not None:
    h,w,c=image.shape
    print(f" height-{h}\n width-{w}\n Colour channel - {c}")
    #Colour channel will be disappear if the image is in greyscale
else:
    print("Error")