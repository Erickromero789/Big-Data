import io
import sys
PATH = '/home/Data'
DIR_DATA = '../Data/'
sys.path.append(PATH) if PATH not in list(sys.path) else None
import os
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from pandas import concat
from sys import getsizeof
filename1 = DIR_DATA + 'ae_com.csv'
filename2 = DIR_DATA + 'amazon_com.csv'
filename3 = DIR_DATA + 'btemptd_com.csv'
filename4 = DIR_DATA + 'calvinklein_com.csv'
filename5 = DIR_DATA + 'hankypanky_com.csv'
filename6 = DIR_DATA + 'macys_com.csv'
filename7 = DIR_DATA + 'shop_nordstrom_com.csv'
filename8 = DIR_DATA + 'us_topshop_com.csv'
filename9 = DIR_DATA + 'victoriassecret_com.csv'
