#Libraries
import os; os.system('clear') #Clean terminal
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Reading data
#########################################################
dataframe = pd.read_csv('Prac_1.csv', index_col = 0)
frequencies = dataframe.columns
dataset = np.array(dataframe)

#Cleaning data
#########################################################
cant_frequencies = len(dataset[0]) #Amount of meditions
X = [] #Coordenates matrix
for n in range(cant_frequencies):
	X.append([]) #Every cicle add a new space to matrix
	for k in range(len(dataset)):
		X[n].append([k+1,dataset[k][n]]) #Add coordenate
X = np.array(X)

#Plotting data
#########################################################
for n in range(cant_frequencies):
	plt.subplot(4,4,n+1)
	plt.plot(X[n][:,0], X[n][:,1])
	plt.title(frequencies[n])
plt.tight_layout(pad=0.001)
plt.show()