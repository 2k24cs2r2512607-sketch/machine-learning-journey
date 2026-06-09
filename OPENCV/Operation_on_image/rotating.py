import cv2
image=cv2.imread("D:\Machine_Learning_Journey\OPENCV\python_Logo.webp")
if image is not None:
    cv2.imshow("Real image",image)
    h,w,c=image.shape
    M=cv2.getRotationMatrix2D((w//2,h//2),90,1.0)
    crop=cv2.warpAffine(image,M,(w,h))
    cv2.imshow("Rotated image",crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not found")