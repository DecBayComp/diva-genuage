import pandas as pd
import numpy  as np

try:
	from   .classifier_utilities import *
except ImportError:
	from   classifier_utilities import *
try:
	from   .utilities import *
except ImportError:
	from   utilities import *

import warnings
import pickle


################################################################################
################################################################################
################################################################################


class combining_RF:


	def __init__(self, full_path_or_features, classifier_path, classification_strength):
		
		self.full_path = full_path_or_features
		self.classifier_path = classifier_path
		self.classification_strength = classification_strength

		try:
			liste_learner      = pickle.load(open(self.classifier_path, 'rb'))
			self.liste_learner = liste_learner
		except FileNotFoundError:
			self.liste_learner = []



	def __prepare_data_for_training__(self):
		
		# separate states (i.e. label tags -- 0 or 1) from features
		state, features                  = prepare_data_equalize_state(self.full_path)
		self.state                       = state
		self.features                    = features
	
		# if no existing classifier is specified, then nothing happens
		if not self.liste_learner:
			pass

		# if an existing classifier is specified, then we perform inference and add log_proba to the features matrix
		else:
			for existing_classifier in self.liste_learner:
				_, log_proba = perform_inference_general(existing_classifier, self.features, 0)
				self.features = np.column_stack((self.features,log_proba[:,1]))



	def __train_RF_classifier__(self):

		classifier_RF, score         = create_the_random_forest_classifier(self.state, self.features)

		if not self.liste_learner:
			self.liste_learner             = [classifier_RF]
		else:
			self.liste_learner.append(classifier_RF)



	def __prepare_data_for_inference__(self):
		
		if not self.liste_learner:
			raise FileNotFoundError("Classifier file not found")

		self.features = self.full_path

		# if only 1 existing classifier is specified, then nothing happens
		if len(self.liste_learner) == 1:
			pass

		# if more than 1 existing classifier is specified, then we perform inference and add log_proba to the features matrix
		else:
			for existing_classifier in self.liste_learner[:-1]:
				_, log_proba = perform_inference_general(existing_classifier, self.features, 0)
				self.features = np.column_stack((self.features,log_proba[:,1]))



	def __predict_proba__(self):

		_, self.log_proba = perform_inference_general(self.liste_learner[-1], self.features, 0)
		return np.exp(self.log_proba[:, 1])


	def __predict_log_proba__(self):

		_, self.log_proba = perform_inference_general(self.liste_learner[-1], self.features, 0)
		return self.log_proba[:, 1]