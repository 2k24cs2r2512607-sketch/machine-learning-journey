import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")

if image is not None:
    pt1=(50,100)
    pt2=(200,400)
    thickness=4
    color=(255,0,0)

    cv2.circle(image,(250,250),50,(0,255,0),thickness=3)
    cv2.imshow("Drawing a circle on image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")
