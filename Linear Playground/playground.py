import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import math



def main(epochs):
    data = pd.read_csv('Linear.csv')
    alpha = 2
    beta =  2
    epsilon = 0.001

    #Normalisation keeps our computations small, especially for gradient descent
    data['X'] = ((data['X'] - data['X'].mean())/data['X'].std())
    data['Y'] = ((data['Y'] - data['Y'].mean())/data['Y'].std())

    for i in range(epochs):
        allLoss = []
        alphaGrad= []
        betaGrad = []

        for row in data.itertuples(index=False):
            prediction  = alpha * row.X + beta
            residual = row.Y - prediction
            loss = residual**2
            alpha_grad = -2 *row.X * residual
            beta_grad = -2 * residual 

            allLoss.append(loss)
            alphaGrad.append(alpha_grad)
            betaGrad.append(beta_grad)

        Loss = sum(allLoss)/len(allLoss)
        alpha -= epsilon * (sum(alphaGrad)/len(alphaGrad))
        beta -= epsilon * (sum(betaGrad)/len(betaGrad))
        print(Loss)
    print(beta)
    print(alpha)
        

main(3100)