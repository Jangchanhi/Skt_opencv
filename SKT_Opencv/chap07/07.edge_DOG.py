import numpy as np, cv2

image = cv2.imread("chap07/images/dog.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")






cv2.imshow("image", image)
cv2.imshow("dst1 - LoG", dst1.astype("uint8"))
cv2.imshow("dst2 - DoG", dst2)
cv2.waitKey(0)
