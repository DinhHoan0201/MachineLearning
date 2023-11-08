from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)
print("Thông tin giữ lại:", X)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca[:, 0], X_pca[:, 1],X_pca[:, 2], c=y, cmap='viridis')
ax.set_xlabel('Chiều 1')
ax.set_ylabel('Chiều 2')
ax.set_ylabel('Chiều 3')
plt.show()
