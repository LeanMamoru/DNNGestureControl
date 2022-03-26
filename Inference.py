import cv2
from preprocessing import hand_extractor
from mouse_control import move_mouse


def start_recognition():
    print("Starting camera ...")
    camera = cv2.VideoCapture(0)
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `width`
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)

    while (True):

        _, frame = camera.read()

        hand_points_image, hand_image, x, y = hand_extractor(frame, width, height)
        if x >= 0 and y >= 0:
            move_mouse(x, y)

        cv2.imshow('Hand skeleton', hand_points_image)

        cv2.imshow('Hand', hand_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_recognition()


