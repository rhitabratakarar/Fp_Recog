import cv2
import numpy


def descriptors(image):

    # apply CLAHE ==> Contrast Limited Adaptive Histogram Equalization

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image = clahe.apply(image)
    image = numpy.array(image, dtype=numpy.uint8) 
    # uint8 = unsigned integer ranging from (0 to 255)


    # Threshold

    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # if pixel image is less than 127, then in matrix its 0 but if higher, then its 255 and hence,

    # Normalize to 0 and 1 range
    image[image == 255] = 1 
    # special feature of numpy arrays (called conditional selection)

    # Applying harris corners to get the keypoints...

    harris_corners = cv2.cornerHarris(image, 3, 3, 0.04)
    harris_normalized = cv2.normalize(harris_corners, 0, 255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32FC1)
    THRESHOLD_HARRIS = 125

    # Extract keypoints

    keypoints = []
    for x in range(0, harris_normalized.shape[0]):
        for y in range(0, harris_normalized.shape[1]):
            if harris_normalized[x][y] > THRESHOLD_HARRIS:
                keypoints.append(cv2.KeyPoint(y, x, 1))
    
    # Define descriptor

    orb = cv2.ORB_create()

    # Compute descriptors

    _, des = orb.compute(image, keypoints)

    # return the keypoints and descriptors...

    return keypoints, des


def match(image_name_1, image_name_2):

    # read image 1 in Gray Scale

    img1 = cv2.imread(image_name_1, cv2.IMREAD_GRAYSCALE)
    _, des1 = descriptors(img1)

    # read image 2 in Gray Scale

    img2 = cv2.imread(image_name_2, cv2.IMREAD_GRAYSCALE)
    _, des2 = descriptors(img2)

    # Match the descriptors that are found by the feature extraction technique

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)


    # Plot keypoints, DO IF NECESSARY DURING PRESENTATION
    # ===================================================================

    # import matplotlib.pyplot as plt
    # img4 = cv2.drawKeypoints(img1, kp1, outImage=None)
    # img5 = cv2.drawKeypoints(img2, kp2, outImage=None)
    # _, axarr = plt.subplots(1, 2)
    # axarr[0].imshow(img4)
    # axarr[1].imshow(img5)
    # plt.show()
    # img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, flags=2, outImg=None)
    # plt.imshow(img3)
    # plt.show()

    # ===================================================================

    # Calculate Sum and Return The Result whether matched or not...

    sum_ = 0
    for m in matches:
        sum_ += m.distance

    SUM_THRESHOLD = 33
    whether_fingerprint_is_valid = (sum_ / len(matches)) < SUM_THRESHOLD

    return whether_fingerprint_is_valid
