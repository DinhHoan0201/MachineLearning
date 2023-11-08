import cv2
import numpy as np

# Hàm tính giá trị LBP cho một pixel trung tâm
def calculate_lbp_value(img, x, y):
    lbp_value = 0
    center = img[y, x]  # Giá trị cường độ của pixel trung tâm

    # Danh sách tọa độ (dx, dy) của 8 pixel hàng xóm
    neighbors = [(-1, -1), (0, -1), (1, -1),
                 (-1, 0),            (1, 0),
                 (-1, 1), (0, 1),  (1, 1)]

    for i, (dx, dy) in enumerate(neighbors):
        # Tọa độ của pixel hàng xóm
        nx, ny = x + dx, y + dy
        # So sánh giá trị cường độ của pixel hàng xóm với giá trị của pixel trung tâm
        if img[ny, nx] >= center:
            lbp_value += 2**i

    return lbp_value

# Đọc hình ảnh và chuyển sang ảnh grayscale
image = cv2.imread(r'C:\Users\Admin\Desktop\Anh\Anh.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Khởi tạo ảnh LBP với cùng kích thước như ảnh grayscale
lbp_image = np.zeros_like(gray_image)

# Tính giá trị LBP cho từng pixel trong ảnh grayscale
for y in range(1, gray_image.shape[0] - 1):
    for x in range(1, gray_image.shape[1] - 1):
        lbp_image[y, x] = calculate_lbp_value(gray_image, x, y)

# Hiển thị ảnh LBP
cv2.imshow('LBP Image', lbp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




