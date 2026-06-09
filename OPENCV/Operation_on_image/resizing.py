import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp") 
if image is None:
    print("Image is not loaded")
else:
    print("Image loaded successfully")
    cv2.imshow("Original Image",image)
    resize=cv2.resize(image,(200,300))#(widthxheigth)
    cv2.imshow("Resized Image",resize)
    
    cv2.imwrite("Resized_image.png",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()