import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")

if image is not None:
    pt1=(50,100)
    pt2=(200,400)
    thickness=3
    color=(255,0,0)

    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("Drawing a rectangle on image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")
    
