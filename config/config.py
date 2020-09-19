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

MAPBOX_TOKEN = 'pk.eyJ1IjoiY2F3aWUiLCJhIjoiY2s1cGVsN3U3MHVrYTNsbnNpd3pubGR3ZSJ9.5sgCAI1IM9pOmmk4dZeD4Q'

today = date.today().isoformat()

