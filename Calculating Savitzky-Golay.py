from math import sqrt
from numpy import concatenate

from matplotlib import pyplot
from pandas import read_csv
from numpy import savetxt
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy as np
from pandas import read_csv
from datetime import datetime

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

dataset = read_csv(r"E:\LUCAS.SOIL_corr.Rdata\ski_wo_artifacts.csv",header=None)

import numpy as np
import scipy.signal as ss
dataset=np.array(dataset)
x=dataset
window_length=101
polyorder=3
sg=ss.savgol_filter(x, window_length, polyorder, deriv=1, delta=1.0, axis=-1, mode='interp', cval=0.0)


np.savetxt('D:\sg_spectral.csv',sg,delimiter=",")
