import cv2  # Import OpenCV library to work with images, videos, and webcams

# Create a VideoCapture object and connect to the default webcam
# 0 means the first/default camera connected to the system
cap = cv2.VideoCapture(0)

# Infinite loop to continuously capture frames from the webcam
while True:

    # Read a frame from the webcam
    # ret   -> Boolean value (True if frame captured successfully, False otherwise)
    # frame -> The actual image/frame captured from the webcam as a NumPy array
    ret, frame = cap.read()

    # Check if frame capture failed
    if not ret:
        print("Could not read frame")
        break  # Exit the loop if webcam is not providing frames

    # Display the captured frame in a window named "Webcam Feed"
    cv2.imshow("Webcam Feed", frame)

    # waitKey(1)
    # - Waits for 1 millisecond for a key press
    # - Returns the ASCII code of the pressed key
    #
    # 0xFF
    # - A mask used to extract the last 8 bits of the returned value
    # - Helps make key detection consistent across different operating systems
    #
    # ord('q')
    # - Converts the character 'q' into its ASCII value (113)
    #
    # Overall meaning:
    # "If the user presses the 'q' key, quit the program"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting............")
        break  # Exit the loop

# Release the webcam resource
# This disconnects the program from the camera
cap.release()

# Close all OpenCV windows created by imshow()
cv2.destroyAllWindows()