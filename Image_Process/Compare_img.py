import cv2
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

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
new_image_path = r'C:\Users\Admin\Desktop\Anh2\Hoannn.png'
new_image = cv2.imread(new_image_path, cv2.IMREAD_GRAYSCALE)
new_hu_features = cv2.HuMoments(cv2.moments(new_image)).flatten()

# Tính toán cosine similarity giữa ảnh mới và các ảnh đào tạo
cosine_similarities = cosine_similarity([new_hu_features], list(train_hu_features.values()))
threshold = 0.95
# Tìm chỉ mục của ảnh đào tạo có cosine similarity lớn nhất
most_similar_image_index = np.argmax(cosine_similarities)

if cosine_similarities[0, most_similar_image_index] > threshold:
    most_similar_image_name = image_names[most_similar_image_index]
    print("Ảnh mới giống nhất với ảnh: {}".format(most_similar_image_name))
else:
    print("Ảnh mới không giống với bất kỳ ảnh nào trong tập đào tạo.")

