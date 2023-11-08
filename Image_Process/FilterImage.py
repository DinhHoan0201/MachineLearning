import  cv2
import  numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\Admin\Desktop\Anh\Anh.jpg')
blur = cv2.blur(img,(15,15))
blur2=cv2.GaussianBlur(img,(5,5),0)
plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Ori')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blur')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(blur2),plt.title('Blurr')
plt.xticks([]),plt.yticks([])
plt.show()

