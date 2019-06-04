import cv2

picks = "Enter 1: To open a video as original and gray\n" \
        "Enter 2: To open an image as original and gray"
print(picks)
user = int(input())
if user == 1:
    print("Two windows will pop up, one is the original video and the other window is the gray video.")
    video = input("Enter in the path to the video.\n"
                  "(For example: C:\\Users\\name\\video.mp4)\n")
    capture = cv2.VideoCapture(video)
    if capture.isOpened() is False:
        print("Error opening the camera")

    # Index to save current frame
    frame_index = 0

    # Read until video is completed
    while capture.isOpened():
        # Capture frame-by-frame from the camera
        ret, frame = capture.read()

        if ret is True:
            # Display the captured frame:
            cv2.imshow('Input frame from the camera', frame)

            # Convert the frame captured from the camera to grayscale:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the grayscale frame:
            cv2.imshow('Grayscale input camera', gray_frame)

            # Press c on keyboard to save current frame
            if cv2.waitKey(20) & 0xFF == ord('c'):
                frame_name = "original{}.png".format(frame_index)
                gray_frame_name = "gray{}.png".format(frame_index)
                cv2.imwrite(frame_name, frame)
                cv2.imwrite(gray_frame_name, gray_frame)
                frame_index += 1

            # Press q on keyboard to exit the program
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        # Break the loop
        else:
            break
    capture.release()
    cv2.destroyAllWindows()
elif user == 2:
    print("Two windows will pop up, one is the original image and the other window is the gray image.")
    image = input("Enter in the path to the image.\n"
                  "(For example: C:\\Users\\name\\image.jpg)\n")
    aImage = cv2.imread(image)
    cv2.imshow("original image", aImage)
    gray_img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("gray image", gray_img)
    cv2.waitKey(0)
else:
    print("Wrong number! Run the program again.")
