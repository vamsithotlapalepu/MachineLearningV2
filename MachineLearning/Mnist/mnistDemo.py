# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:09:18 2020

@author: vamsi
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = pd.read_csv("mnist_train.csv")
    l = data['label']
    d0 = data.drop("label",axis=1)
    print(d0.shape)
    print(l.shape)
    test =40
    #matrix = d0.iloc[2].as_matrix().reshape(28,28)
    matrix = d0.iloc[test].values.reshape(28,28)
    print(l[test])
    plt.figure(figsize=(7,7))
    plt.imshow(matrix)
    plt.show()
    
if(__name__=="__main__"):
    main()