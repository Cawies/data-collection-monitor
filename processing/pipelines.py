# External libraries
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from datetime import *
import requests
import json

# Internal modules
import preprocessors as pp
from config import config


anomaly_detection_pipeline = Pipeline(
    [
        (
            "short_descriptive_label",
                pp.PipelineStepOne(variables=config.SPECIFIED_VARIABLES),
        ),
        (
            "short_descriptive_label",
                pp.PipelineStepTwo(variables=config.SPECIFIED_VARIABLES)
        )
    ]
)