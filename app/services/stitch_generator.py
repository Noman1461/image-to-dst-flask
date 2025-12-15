import cv2

def extract_contours(binary_image):
    """
    Extracts contours from binary image.
    """
    contours, _ = cv2.findContours(
        binary_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours

def contours_to_stitches(contours, scale=1):
    """
    Convert contours into stitch points.
    """
    stitches = []

    for contour in contours:
        for point in contour:
            x, y = point[0]
            stitches.append((int(x * scale), int(y * scale)))

        # END stitch between contours
        stitches.append(("END",))

    return stitches
