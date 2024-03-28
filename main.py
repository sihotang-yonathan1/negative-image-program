import pathlib

import cv2
import cv2.typing

def _create_negative_image(image_path: pathlib.Path | str, bit_max_value: int = 255) -> cv2.typing.MatLike:
    """
    @params image_path      pathlib.Path | str  image source path
    @params bit_max_value   int                 Maximal bit value for a pixel (usually unsigned int 8 -> 255)
    
    This function process image based `image_path` and `bit_max_value` parameter and change the image
    into the negative form and returns the processed image
    """
    # read the image file
    image_matrix = cv2.imread(str(image_path))
    
    # filter the image: 255 - current_pixel
    negative_image_matrix = bit_max_value - image_matrix

    # show the result
    cv2.imshow('Input image', image_matrix)
    cv2.imshow('Negative image', negative_image_matrix)

    # Set the image window keep open
    cv2.waitKey(0)

    # return the matrix to process further
    return negative_image_matrix


def main() -> None:
    # Ask user to name the output image
    output_filename = input('Output path (with extension): ')

    # create negative image using `_create_negative_image`
    negative_image_matrix = _create_negative_image(pathlib.Path('./assets/monako-5.jpg'))
    
    # write image to disk
    cv2.imwrite(output_filename, negative_image_matrix)

     # destroy the window after use
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # execute `main` function when run directly (not as module)
    main()