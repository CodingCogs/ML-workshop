#Import pickle and os:

import pickle
import os

#Create a class object and name it NN_Model:

class NN_Model(object):
	""" docstring for TrainedModel:
		Inside of the class, create an initializer method that loads the file containing the
		saved model (model_exercise.pkl) into the code:
	"""
	def __init__(self):
		path = os.getcwd()+'/model_exercise.pkl'
		file = open(path, 'rb')
		self.model = pickle.load(file)
	
	# Inside the class named NN_Model, create a predict method. It should take in
	# the feature values and input them as arguments to the predict method of the
	# model so that it can feed them into the model and make a prediction:

	def predict(self, season, age, childish, trauma, surgical, fevers, alcohol, smoking, sitting):
		X = [[season, age, childish, trauma, surgical, fevers, alcohol, smoking, sitting]]
		return self.model.predict(X)