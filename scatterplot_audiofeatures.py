"""
This program plots the various charts and graph of the audio features of Tabla strokes.
Makes it easy for the analysis of the audio features.


@author: Subodh D.
"""

import pandas as pd
import matplotlib.pyplot as plt


mydata = pd.read_csv("all_strokes.csv")
# import custom data and label
y = mydata["output"]  #provided your csv has header row, and the label column is named "Label"

#select all but the last column as data
X = mydata.iloc[:,:-1]

df = mydata.iloc[:,[3, 4]]
df.plot()  # plots all columns against index
df.plot(kind='scatter',x='Mean_Mem20_MFCC0_Power_powerFFT_WinHamming_HopSize512_WinSize512_Sum_AudioCh0',
        y='Mean_Mem20_Flux_Power_powerFFT_WinHamming_HopSize512_WinSize512_Sum_AudioCh0') # scatter plot
df.plot(kind='density')  # estimate density function
df.plot(kind='hist')     # histogram


plt.show()
