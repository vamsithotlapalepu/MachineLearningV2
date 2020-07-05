# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:09:18 2020

@author: vamsi
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    data = pd.read_csv("mnist_train.csv")
    l = data['label']
    d0 = data.drop("label",axis=1)
    print(d0.shape)
    print(l.shape)
    test =189
    #matrix = d0.iloc[2].as_matrix().reshape(28,28)
    matrix = d0.iloc[test].values.reshape(28,28)
    print(l[test])
    plt.figure(figsize=(7,7))
    plt.imshow(matrix,cmap="gray")
    plt.show()
    
if(__name__=="__main__"):
    main()