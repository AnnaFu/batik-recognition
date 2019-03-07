import cv2
import numpy as np
import os
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *

def doing(image_paths):
	# Load the classifier, class names, scaler, number of clusters and vocabulary 
	clf, classes_names, stdSlr, k, voc = joblib.load("bof.pkl")

	# Create feature extraction and keypoint detector objects
	sift = cv2.xfeatures2d.SIFT_create()

	# List where all the descriptors are stored
	des_list = []

	for image_path in image_paths:
		im = cv2.imread(image_path)
		if im == None:
			print("No such file {}\nCheck if the file exists", image_path)
			exit()
		kpts, des = sift.detectAndCompute(im, None)
		des_list.append((image_path, des)) 
    
	# Stack all the descriptors vertically in a numpy array
	descriptors = des_list[0][1]
	for image_path, descriptor in des_list[0:]:
		descriptors = np.vstack((descriptors, descriptor)) 

	# 
	test_features = np.zeros((len(image_paths), k), "float32")
	for i in range(len(image_paths)):
		words, distance = vq(des_list[i][1],voc)
		for w in words:
			test_features[i][w] += 1

	# Perform Tf-Idf vectorization
	nbr_occurences = np.sum( (test_features > 0) * 1, axis = 0)
	idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

	# Scale the features
	test_features = stdSlr.transform(test_features)

	# Perform the predictions
	predictions =  [classes_names[i] for i in clf.predict(test_features)]
	return predictions[0]
	