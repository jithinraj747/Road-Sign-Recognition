## Road-Sign-Recognition

A deep learning CNN (Convoluted Neural Network) model was build for identifying road and traffic signs using Keras and OpenCV. The dataset for model building was obtained from Kaggle. It consists of 58 traffic/road signs each labeled from 0-57. The data is a mixture of regulatory, cautionary and indication signs. Overall, there are around 4170 images. The dataset is located in the 'traffic_Data' sub-folder of the 'archive' directory. The labels for the dataset 'labels.csv' is provided in the same directory. Most of these images are similarly sized and are close up shots of traffic sign boards taken from the streets and roads. This provides the opportunity to make use of image localization during image pre-processing and object detection (using computer vision). 





OpenCV was used for image localization and pre-processing of dataset images during model building as well as for image detection and pre-processing during prediction. 'Road Sign Recognition 1.ipynb' and 'Road Sign Recognition 2.ipynb' are codes for model buuilding and preliminary testing respectively. The model was saved as 'road_sign_recognition' and was relocated to the 'Testing' directory. 




A threshold value of 85% was set for prediction which means that only those model predictions greater than 85% will be displayed in the output. 
