import cv2 as cv
from pathlib import Path

# project_folder = Path(__file__).parent.parent
# img_path = project_folder / "assets" / "basketball.jpg"

# img = cv.imread(img_path)

# small = cv.resize(img, None, fx=0.5, fy=0.5)

video = cv.VideoCapture(1)

while True:

    # Returns true if there is no frame
    isTrue, frame = video.read()

    if not isTrue:
        break

    # # For better tracking
    # frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # lower = (5, 100, 100)
    # upper = (25, 255, 255)

    # Hough circles only uses grayscale
    frame_GRAY = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # GaussianBlur Sharpens edges
    # ksize -> kernel size is the area of pixels to look at
    # sigmaX -> controls amount of blur

    frame_GRAY = cv.GaussianBlur(frame_GRAY, (3, 3), 2)

    # cv.HOUGH_GRADIENT -> algorithim
    # dp=1 means that each pixel gets their own vote for edge
    # increasing dp means process is faster but less accurate
    # param1 conrtols strictness of edges
    # param2 -> confidence of circle

    circles = cv.HoughCircles(frame_GRAY, cv.HOUGH_GRADIENT, dp=1, minDist=600,
                              param1=100, param2=40, minRadius=20, maxRadius=70)

    if circles is not None:
        circles = circles[0].astype(int)

        for x, y, r in circles:

            # Draws outer circle (BGR) blue
            cv.circle(frame, (x, y), r, (255, 0, 0), 8)
            #        img      cor    r  color        thickness

            # Draws center
            cv.circle(frame, (x, y), 2, (0, 0, 0), 3)

    # Displays frame
    cv.imshow('Basketball free throw', frame)

    # waits 20 milliseconds and checks if user pressed q
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
