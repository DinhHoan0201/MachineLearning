import cv2
import numpy as np
import os
from scipy.stats import pearsonr

# Thư mục chứa ảnh đào tạo
train_data_dir = r'C:\Users\Admin\Desktop\Anh'

# Đọc và tính toán đặc trưng HU cho mỗi ảnh đào tạo
train_images = []
train_hu_features = {}
image_names = []

for filename in os.listdir(train_data_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(train_data_dir, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        hu_moments = cv2.HuMoments(cv2.moments(image)).flatten()

        train_images.append(image)
        train_hu_features[filename] = hu_moments
        image_names.append(filename)

# Ảnh mới để kiểm tra
new_image_path = r'C:\Users\Admin\Desktop\Anh2\nghia1.jpg'
new_image = cv2.imread(new_image_path, cv2.IMREAD_GRAYSCALE)
new_hu_features = cv2.HuMoments(cv2.moments(new_image)).flatten()

# Tính toán Pearson correlation coefficient giữa ảnh mới và các ảnh đào tạo
correlation_coefficients = [pearsonr(new_hu_features, feature)[0] for feature in train_hu_features.values()]

# Đặt ngưỡng (threshold)
threshold = 0.95  # Điều chỉnh ngưỡng theo ý muốn

# Tìm chỉ mục của ảnh đào tạo có Pearson correlation coefficient cao nhất
most_similar_image_index = np.argmax(correlation_coefficients)

if correlation_coefficients[most_similar_image_index] > threshold:
    most_similar_image_name = image_names[most_similar_image_index]
    print("Ảnh mới giống nhất với ảnh: {}".format(most_similar_image_name))

    # Chỉnh kích thước ảnh mới và ảnh giống nhau
    new_image_resized = cv2.resize(new_image, (300, 300))  # Chỉnh kích thước thành 300x300 (có thể điều chỉnh)
    similar_image_resized = cv2.resize(train_images[most_similar_image_index], (300, 300))  # Chỉnh kích thước thành 300x300 (có thể điều chỉnh)

    # Hiển thị ảnh gốc và ảnh giống nhau
    cv2.imshow('Ảnh Gốc', new_image_resized)
    cv2.imshow('Ảnh Giống Nhất', similar_image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Ảnh mới không giống với bất kỳ ảnh nào trong tập đào tạo.")
