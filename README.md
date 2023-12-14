# MRI-Image-Segmentation
This Python script utilizes the KMeans clustering algorithm to perform color-based segmentation on MRI brain images. The goal is to identify dominant colors within the image, assisting in the visualization and analysis of different anatomical structures or abnormalities present in the MRI scans.
## **Usage**  

Clone the repository:  
`
bash git clone https://github.com/your-username/mri-image-segmentation.git
`  

Navigate to the project directory:  
`bash cd mri-image-segmentation`

Install the required libraries:  
(not yet implemented)
`bash pip install -r requirements.txt`

Run the script:  
`bash python mri_segmentation.py
`  

Make sure to replace **"mri.jpg"** with the path to your own MRI image.  


## **Results**
The script outputs the dominant colors found in the MRI image, providing a palette representing different tissue types or image features. The segmented image visually highlights the distinct regions identified through color clustering. The segmented images can be integrated into ML/DL for tasks such as image segmentation, classification, or object detection. The color clusters can serve as informative features, aiding neural networks in learning meaningful representations from the MRI data.

## **Parameters**
Adjust the num_colors variable to control the number of clusters used for color segmentation. The recommended range is 3-5 for simple MRI and 6-10 for contrast-enhanced MRI.  

## **Example**
![image](https://github.com/DaniCoimbra/MRI-Image-Segmentation/assets/111929276/1a1a1314-6798-464f-873e-c9f55637fbc2)  
Script Running 4 clusters on simple MRI brain


