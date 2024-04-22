from PIL import Image
Image.open('car.jpg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 

image = mpimg.imread('car.jpg')
w, h, d = tuple(image.shape)
pixels = np.reshape(image, (w * h, d))
from sklearn.cluster import KMeans
n_colors = 5 #change this to get few more colors
model = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
paletter = np.uint8(model.cluster_centers_)
plt.imshow([palette])
plt.show()
