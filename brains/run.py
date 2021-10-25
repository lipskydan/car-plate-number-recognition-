from model import *
from plate_detection_tools import *


def recognise_plate(img_path):
    img = cv2.imread(img_path)
    display(img, 'input image')

    output_img, plate = detect_plate(img)
    display(output_img, 'detected license plate in the input image')

    char = segment_characters(plate)

    print(f'plate number is {show_results(char=char)}')


if __name__ == "__main__":
    recognise_plate('images/car6.jpeg')
