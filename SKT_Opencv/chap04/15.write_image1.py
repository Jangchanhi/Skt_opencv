import cv2

image = cv2.imread("chap04/images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러") # 예외처리
    
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)        # JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]       # png 압축 레벨 설정

## 행렬을 영상 파일로 저장
cv2.imwrite("images/write_test1.jpg", image)       # 디폴트는 95
cv2.imwrite("images/write_test2.jpg", image, params_jpg) # 지정한 화질로 저장
cv2.imwrite("images/write_test3.png", image, params_png )
cv2.imwrite("iamges/write_test4.bmp", image)         # 
print("저장 완료")