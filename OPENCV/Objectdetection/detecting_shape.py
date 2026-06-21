import cv2

# Read image
img = cv2.imread(r"D:\Machine_Learning_Journey\OPENCV\aa - Copy.png")

if img is None:
    print("Error: Image not found!")
    exit()

# Keep original image safe
output = img.copy()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold image
_, thresh = cv2.threshold(
    gray,
    200,
    255,
    cv2.THRESH_BINARY_INV
)

# Find only external contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:

    # Ignore tiny contours (noise)
    area = cv2.contourArea(contour)

    if area < 100:
        continue

    # Approximate contour
    approx = cv2.approxPolyDP(
        contour,
        0.02 * cv2.arcLength(contour, True),
        True
    )

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        shape_name = "Rectangle"

    elif corners == 5:
        shape_name = "Pentagon"

    else:
        shape_name = "Circle"

    # Draw contour
    cv2.drawContours(
        output,
        [approx],
        -1,
        (0, 255, 0),
        3
    )

    # Find position for text
    x, y, w, h = cv2.boundingRect(approx)

    cv2.putText(
        output,
        shape_name,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Detected Shapes", output)

cv2.waitKey(0)
cv2.destroyAllWindows()