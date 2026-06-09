import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is not None:
    cv2.imshow("Image showing",image)  #Open the window
    cv2.waitKey(0) #wait for a key
    cv2.destroyAllWindows()#Close the window
else:
    print("Image not loaded")