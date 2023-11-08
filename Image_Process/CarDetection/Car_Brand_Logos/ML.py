import cv2
import os
import numpy as np
# Đường dẫn đến thư mục chứa dữ liệu
dataset_folder = r'Train'
test_folder = r'Test'
# Khởi tạo trình trích xuất đặc trưng SIFT với số lượng keypoints giới hạn
sift = cv2.SIFT_create(nfeatures=500)

# Duyệt qua từng ảnh trong thư mục test
for folder_name in os.listdir(test_folder):
    folder_path = os.path.join(test_folder, folder_name)

    # Kiểm tra xem folder có phải là thư mục không
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            test_image_path = os.path.join(folder_path, filename)

            # Đọc ảnh đầu vào cần nhận dạng và chuyển đổi thành ảnh grayscale nếu cần
            input_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)

            # Kiểm tra xem ảnh có đọc được và có kiểu dữ liệu và chiều sâu đúng không
            if input_image is None:
                print(f"Không thể đọc ảnh: {test_image_path}")
            elif input_image.dtype != np.uint8:
                print(f"Kiểu dữ liệu không đúng cho ảnh: {input_image.dtype}")
            else:
                # Trích xuất đặc trưng SIFT của ảnh đầu vào
                keypoints_input, descriptors_input = sift.detectAndCompute(input_image, None)

                # Lưu trữ điểm khớp tốt nhất và khoảng cách tương ứng
                best_match = None
                best_distance = float('inf')

                # Duyệt qua các thư mục con trong dataset_folder
                for folder_name in os.listdir(dataset_folder):
                    folder_path = os.path.join(dataset_folder, folder_name)

                    # Kiểm tra xem folder có phải là thư mục không
                    if os.path.isdir(folder_path):
                        for filename in os.listdir(folder_path):
                            sample_image_path = os.path.join(folder_path, filename)

                            # Đọc ảnh mẫu và trích xuất đặc trưng SIFT
                            sample_image = cv2.imread(sample_image_path, cv2.IMREAD_GRAYSCALE)
                            keypoints_sample, descriptors_sample = sift.detectAndCompute(sample_image, None)

                            # Matching đặc trưng giữa ảnh đầu vào và ảnh mẫu
                            bf = cv2.BFMatcher()
                            matches = bf.knnMatch(descriptors_input, descriptors_sample, k=2)

                            # Áp dụng xét định Goodman để lọc các điểm khớp tốt
                            good_matches = []
                            for m, n in matches:
                                if m.distance < 0.75 * n.distance:
                                    good_matches.append(m)

                            # Tính tổng khoảng cách của các điểm khớp
                            total_distance = sum(match.distance for match in good_matches)

                            # So sánh tổng khoảng cách với khoảng cách tốt nhất hiện tại
                            if len(good_matches) > 0:
                                average_distance = total_distance / len(good_matches)
                                if average_distance < best_distance:
                                    best_distance = average_distance
                                    best_match = folder_name

                # In ra kết quả cuối cùng cho từng ảnh
                if best_match is not None:
                    print(f"Ảnh {test_image_path}: Hãng nhận dạng: {best_match}")
                else:
                    print(f"Ảnh {test_image_path}: Không nhận dạng được.")
