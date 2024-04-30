#fleiss.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Solomiia Korol
based on the code of @Shamya on GitHub
"""

def checkInput(rate, n):
    """ 
    Check correctness of the input matrix
    @throws AssertionError 
    """
    N = len(rate)
    k = len(rate[0])
    assert all(len(rate[i]) == k for i in range(k)), "Row length != #categories)"
    assert all(isinstance(rate[i][j], int) for i in range(N) for j in range(k)), "Element not integer" 


def fleissKappa(rate,n):
    """ 
    Computes the Kappa value
    @param rate - ratings matrix containing number of ratings for each subject per category 
    [size - N X k where N = #subjects and k = #categories]
    @param n - number of raters   
    @return fleiss' kappa
    """

    N = len(rate)
    k = len(rate[0])
    print("#raters = ", n, ", #subjects = ", N, ", #categories = ", k)
    checkInput(rate, n)
    
    # mean of squares of proportion of all assignments which were to jth category
    PE = sum([j**2 for j in [sum([rows[i] for rows in rate])/(N*n) for i in range(k)]])
    print("PE =", PE)
    
    #mean of the extent to which raters agree for the ith subject 
    PO = sum([(sum([i**2 for i in row])- n) / (n * (n - 1)) for row in rate])/N
    print("PO = ", PO)
    
    kappa = -float("inf")
    try:
        kappa = (PO - PE) / (1 - PE)
        kappa = float("{:.3f}".format(kappa))
    except ZeroDivisionError:
        print("Expected agreement = 1")

    print("Fleiss' Kappa =", kappa)
    
    return kappa