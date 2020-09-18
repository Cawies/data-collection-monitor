# External libraries
import os
import pathlib
from datetime import *



DASHBOARD_TITLE = ''

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASET_DIR = f"{PACKAGE_ROOT}/output_data"
DATA_FILE = ''

# Specify which (if any) variables of whole dataset to keep/drop
VARIABLES = []
DROP_VARIABLES = []

# Specify which variables to be used in pipeline steps
VARS_STEP_ONE = []
VARS_STEP_TWO = []
VARS_STEP_THREE = []
VARS_STEP_FOUR = []


today = date.today().isoformat()

