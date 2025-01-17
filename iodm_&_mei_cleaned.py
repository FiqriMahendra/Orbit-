# -*- coding: utf-8 -*-
"""IODM & MEI cleaned

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OS4MdK5niIXA4FMV4-AUzUe4Uq53Ds3J

# Flattening IODM and MEI V2 and save dataset to **Cleaned** folder
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
 
import warnings
warnings.filterwarnings('ignore')
 
from google.colab import drive
drive.mount("/content/gdrive")

"""# Flattening IODM values

check IODM values
"""

IODM_Raw = pd.read_csv(r'/content/gdrive/MyDrive/Project/Ocean Index vs Local Climate/Dataset IODM 2.csv', error_bad_lines=False, sep=';',index_col= False )
IODM_Raw

"""Drop years column and starting flattening process"""

#Importing the dataset 
df_IODM = pd.read_csv(r'/content/gdrive/MyDrive/Project/Ocean Index vs Local Climate/Dataset IODM 2.csv', error_bad_lines=False, sep=';',index_col= False )
df_IODM.drop('Years',axis='columns', inplace=True)
df_IODM

df_IODM_flat = df_IODM.values.flatten()
df_IODM_flat

# Save the flattened IODM
output_array = np.array(df_IODM_flat)
np.savetxt("/content/gdrive/MyDrive/Project/Cleaned/df_IODM_cleaned.csv", output_array, delimiter=";")

"""# Flattening MEI V2 values"""

#Import the dataset and drop years information
df_MEI = pd.read_csv(r'/content/gdrive/MyDrive/Project/Ocean Index vs Local Climate/Dataset MEI V2.csv', error_bad_lines=False, sep=';')
df_MEI.drop('Year',axis='columns', inplace=True)
df_MEI
#len(df_MEI)

"""Flattening the MEI V2 dataset and save flattened dataset"""

df_MEI_flat = df_MEI.to_numpy().flatten()
df_MEI_flat

import numpy as np

output_array = np.array(df_MEI_flat)
np.savetxt("/content/gdrive/MyDrive/Project/Cleaned/df_MEI_cleaned.csv", output_array, delimiter=";")