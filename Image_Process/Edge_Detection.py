import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread(r'C:\Users\Admin\Desktop\Anh2\nghia1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise (optional)
image_blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Calculate the Laplacian of the blurred image
laplacian = cv2.Laplacian(image_blurred, cv2.CV_64F)

# Convert the Laplacian image to uint8 format
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Display the results
cv2.imshow('Original', image)
cv2.imshow('Laplacian Edges', laplacian_abs)

cv2.waitKey(0)
cv2.destroyAllWindows()
