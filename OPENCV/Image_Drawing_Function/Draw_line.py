import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")

if image is not None:
    pt1=(50,100)
    pt2=(200,400)
    thickness=4
    color=(255,0,0)

    cv2.line(image,pt1,pt2,color,thickness=3)
    cv2.imshow("Coloured image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
