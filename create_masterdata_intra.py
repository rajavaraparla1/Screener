"""
    This needs to be run at 9:15 or 9:30 AM Daily.
    This will create advances and declines for each index.
"""

from nsetools import Nse
from conf import  constants
import pandas as pd
from utils import xls_utils

xls_utils.write_advdec_to_excel(constants.INTRA_ANALYSIS_FILE,"advdec",2)

