import sympy
import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

###Create a TAD of legnth M+1###

def create_TAD(M):
    X=np.zeros((M+1))
    return X

###Increment the ith cell of the TAD###

def put_in_TAD(X, i):
    X[i] += 1

###Evaluates the TAD, gives the min, max, mean and the occurence of each values###

def evaluate_TAD(X, M, graph):
    print(graph)
    nb_acces = np.count_nonzero(X[0:M])
    labels, values = zip(*Counter(X[0:M]).items())
    ## A ORDONNER
    print(labels)
    indexes = np.arange(len(labels))
    width = 1
    print(indexes)
    print(values)
    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    if (graph == 2):
        plt.tight_layout() ##auto scale
        plt.show()
    mean = np.ndarray.mean(X[0:M])
    min = np.ndarray.min(X[0:M])
    max = np.ndarray.max(X[0:M])
    for i in range(int(max+1)):
        print("there are: ", np.count_nonzero(X == i),i  )
    print("number access: ", nb_acces, "|mean: ", mean, "|min: ", min, "|max:", max)


###increment a random cell of the TAD and increment the counter

def use_TAD(X, M, R):
    for i in range(R):
        X[M] +=1
        j = random.randint(0, M-1)
        put_in_TAD(X, j)

###gerenarte a Prime number close to M

def generate_prime_number(M):
    min = M- 0.20*M
    max = M+ 0.20*M
    primeM = sympy.randprime(min, max)
    print(primeM)

def hash_justin_maxence(primeM, string):
    string_inbyte = bytes(string, 'utf-8')
    print(string_inbyte)








