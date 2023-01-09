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
import argparse


################################################################################
################################################################################
################################################################################


class combining_classifiers:

	# search for existing learner ; create new one if doesn't exist
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
			self.__recreate_all_features_from_previous_learners__()



	def __prepare_data_for_inference__(self):
		
		if not self.liste_learner:
			raise FileNotFoundError("Classifier file not found")

		self.features = self.full_path



	def __apply_multiple_classifier_to_features__(self, c5=False):

		
		if self.classification_strength >1:

			classifier_1, score      = create_the_random_forest_classifier(self.state, self.features)
			classifier_2, score      = create_adaboost_classifier_tree(self.state, self.features)
			classifier_3, score      = create_adaboost_classifier_SGD(self.state, self.features)
			classifier_4, score      = create_catboost_classifier(self.state, self.features)
			if c5:
				classifier_5, score      = create_the_gaussian_process_classifier(self.state, self.features)
				self.set_classifier      = {'c1': classifier_1, 'c2':classifier_2, 'c3':classifier_3, 'c4':classifier_4, 'c5':classifier_5}

			else:
				self.set_classifier      = {'c1': classifier_1, 'c2':classifier_2, 'c3':classifier_3, 'c4':classifier_4}

			self.features            = create_new_features_from_weak_classifiers(self.set_classifier, self.features)



	def __apply_main_classifier__(self, classif=None):


		if self.classification_strength == 10:
			classif = 'gpc'

		elif self.classification_strength == 1:
			classif = 'rf'

		if classif == 'rf':
			classifier_main, score      = create_the_random_forest_classifier(self.state, self.features)

		elif classif == 'ada_tree':
			classifier_main, score      = create_adaboost_classifier_tree(self.state, self.features)

		elif classif == 'ada_sgd':
			classifier_main, score      = create_adaboost_classifier_SGD(self.state, self.features)

		elif classif == 'catboost':
			classifier_main, score      = create_catboost_classifier(self.state, self.features)

		elif classif == 'gpc':
			classifier_main, score      = create_the_gaussian_process_classifier(self.state, self.features)

		else:
			classifier_main, score      = create_xgboost_classifier(self.state, self.features)


		state_out, log_proba     = perform_inference_general(classifier_main, self.features, 0)

		try:
			self.set_classifier['main']    = classifier_main
		except AttributeError:
			self.set_classifier = {'main': classifier_main}
		

		if not self.liste_learner:
			self.liste_learner             = [self.set_classifier]
		else:
			self.liste_learner.append(self.set_classifier)



	def __recreate_all_features_from_previous_learners__(self):

		liste_learner = self.liste_learner
		features      = self.features
		for dict_classif_loc in liste_learner:
			log_proba,_,features =  perform_inference_all_classifiers(dict_classif_loc, features)
		self.features  = features
		self.log_proba = log_proba



	def __predict_log_proba__(self):

		self.__recreate_all_features_from_previous_learners__()

		return self.log_proba



	def __predict_proba__(self):

		self.__recreate_all_features_from_previous_learners__()

		return np.exp(self.features[:,-1])