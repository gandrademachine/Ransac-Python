import numpy as np
import matplotlib.pyplot as plt
from random import sample

def euclidianError():

def Ransac(data, model, minimumpts, maxitr, threshold, assertive):
    
    itr = 0;
    bestFitting = Null
    bestError = 1e1000
    while itr < maxitr:
        possibleInliers = sample(data,minimumpts)
        maybeModel = model(possibleInliers)
        alsoInliers = []
        for i in maybeInliers:
            if np.linalg.norm(i-maybeModel[maybeInliers.index(i)]) < threshold:
                alsoInliers.append(i)
        if len(alsoInliers) > closedata :
             betterModel = [*maybeModel, *alsiInliers]
             thisError = np.mean(np.linalg.norm(betterModel - data, axis = 0)) 
             if thisError < bestError :
                 bestFitting = betterModel
                 bestError = ThisError
        itr += 1
    return bestFitting

sample = 100
data = np.random.random((sample,2))
model
