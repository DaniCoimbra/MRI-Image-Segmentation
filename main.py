import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Image path then use opencv2 library to read image
image_path = "mri.jpg"

image = cv2.imread(image_path)


#Brain MRI using 3-5 colors clusters for simple MRI, 6-10 for contrast MRI
num_colors = 4

#Convert the image from BGR to RGB and reshape as a list of pixels
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixels = image.reshape((-1, 3))

#KMeans clustering to get dominant colors
kmeans = KMeans(n_clusters=num_colors)
kmeans.fit(pixels)

#Get the dominant colors
dominant_colors = kmeans.cluster_centers_.astype(int)

print("Dominant Colors:", dominant_colors)

# KMeans clustering to get labels for each pixel
kmeans = KMeans(n_clusters=num_colors)
labels = kmeans.fit_predict(pixels)

# Reshape the labels to match the image shape
segmented_image = labels.reshape(image.shape[:2])

#Display the original and segmented images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.imread(image_path))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='viridis')
plt.title("Segmented Image")

plt.show()
