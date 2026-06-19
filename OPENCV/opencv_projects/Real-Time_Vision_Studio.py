import cv2
camera = cv2.VideoCapture(0)
saved_frame = 0
save_message_counter = 0  # Controls how long "Frame Saved!" is shown
gray_scale=False
flip_mode=False
Blur_Mode=False
while True:
    ret, frame = camera.read()
    if not ret:
        print("Error... Could not read frame")
        break
    # Instructions
    cv2.putText(frame, "G : Grayscale Mode", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.putText(frame, "F : Flip Mode", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.putText(frame, "N : Normal Mode", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.putText(frame, "S : Save Frame", (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, "B : Blur Mode", (10, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.putText(frame, "Q : Quit", (10, 190),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
     
    if gray_scale:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if flip_mode:
        frame=cv2.flip(frame,0)
    if Blur_Mode:
        frame=cv2.GaussianBlur(frame, (15, 15), 0)
    # Show save message for some frames
    if save_message_counter > 0:
        cv2.putText(frame, "Frame Saved!", (400, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 0), 2)
        save_message_counter -= 1

    # Show webcam feed
    cv2.imshow("Capturing Video", frame)

    # Read keyboard input
    key = cv2.waitKey(1) & 0xFF

    # Save frame
    if key in {ord('s'),ord('S')}:
        saved_frame += 1

        filename = f"SavedFrame{saved_frame}.png"

        cv2.imwrite(filename, frame)

        print(f"{filename} saved successfully")

        # Show message for ~2 seconds
        save_message_counter = 60

    # Quit
    elif key in {ord('q'),ord('Q')}:
        print("Quitting.....")
        break
    elif key in {ord('G'),ord('g')}:
        gray_scale=True
    elif key in {ord('F'),ord('f')}:
        flip_mode=True
    elif key in {ord('n'),ord('N')}:
        flip_mode=False
        gray_scale=False
        Blur_Mode=False
    elif key in {ord('B'),ord('b')}:
        Blur_Mode=True
   


camera.release()
cv2.destroyAllWindows()
 