## Road-Sign-Recognition

A deep learning CNN (Convoluted Neural Network) model was build for identifying road and traffic signs using Keras and OpenCV. The dataset for model building was obtained from Kaggle. It consists of 58 traffic/road signs each labeled from 0-57. The data is a mixture of regulatory, cautionary and indication signs. Overall, there are around 4170 images. The dataset is located in the 'traffic_Data' sub-folder of the 'archive' directory. The labels for the dataset 'labels.csv' is provided in the same directory. Most of these images are similarly sized and are close up shots of traffic sign boards taken from the streets and roads. This provides the opportunity to make use of image localization during image pre-processing and object detection (using computer vision). 

<br>
<p align='center'>
  <img src="https://github.com/jithinraj747/Road-Sign-Recognition/assets/106642456/c64f066d-6c04-420b-b998-1331eeb728da" width=400>
</p> <br>




'Road Sign Recognition 1.ipynb' and 'Road Sign Recognition 2.ipynb' constitutes the codes for model buuilding and preliminary testing respectively. The model was saved as 'road_sign_recognition' and was relocated to the 'Testing' directory. 

<br>
<p align='center'>
  <img src="https://github.com/jithinraj747/Road-Sign-Recognition/assets/106642456/89557142-22a4-4f12-bfdb-e118a5873fc9" width=400>
</p> <br>

<br>
<p align='center'>
  <img src="https://github.com/jithinraj747/Road-Sign-Recognition/assets/106642456/922a1f8c-d441-4900-ae97-b7d1f64e0ea7" width=400>
</p> <br>

A threshold value of 85% was set for prediction which means that only those model predictions greater than 85% will be displayed in the output. 

<br>
<p align='center'>
  <img src="https://github.com/jithinraj747/Road-Sign-Recognition/assets/106642456/27d4deb6-eae5-496a-9e48-3b24e52b2e94" width=400>
</p> <br>
