import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")

if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded")