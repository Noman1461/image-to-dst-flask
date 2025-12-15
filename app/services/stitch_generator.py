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

def contours_to_stitches(contours, scale=0.3):
    """
    Convert contours into stitch paths.
    Returns list of (x, y, command)
    """
    stitches = []

    for contour in contours:
        first = True
        for point in contour:
            x, y = point[0]
            x = int(x * scale)
            y = int(y * scale)

            if first:
                stitches.append((x, y, "JUMP"))
                first = False
            else:
                stitches.append((x, y, "STITCH"))

    return stitches

