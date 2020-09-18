# External libraries
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import requests
import json




class PipeLineStepOne(BaseEstimator, TransformerMixin):
	''' Brief description of what this transformer class does'''

	def __init__(self, variables=None):
		if not isinstance(variables, list):
			self.variables = [variables]
		else:
			self.variables = variables

	def fit(self, X: pd.DataFrame, y: pd.Series=None):
		''' This method is only to accomodate sklearn class format '''
		return self


	def transform(self, X: pd.DataFrame):
		''' This method specifies what transformations will be done to specified data. '''

		X = X.copy()


		# Define your method here with respect to X.


		return X

class PipeLineStepTwo(BaseEstimator, TransformerMixin):
	''' Brief description of what this transformer class does'''

	def __init__(self, variables=None):
		if not isinstance(variables, list):
			self.variables = [variables]
		else:
			self.variables = variables

	def fit(self, X: pd.DataFrame, y: pd.Series=None):
		''' This method is only to accomodate sklearn class format '''
		return self


	def transform(self, X: pd.DataFrame):
		''' This method specifies what transformations will be done to specified data. '''

		X = X.copy()


		# Define your method here with respect to X.


		return X


# Etc... 